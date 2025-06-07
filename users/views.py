from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .forms import UserForm,LocationForm,ProfileForm

def login_view(request):
    if request.method=="POST":
        login_form=AuthenticationForm(request=request,data=request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data.get('username')
            password=login_form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f'You are now logged in as {username}')
                return redirect('home')
        else:
            messages.error(request,f'An error occured while you are logging')
    else:
        login_form=AuthenticationForm()
    return render(request,'views/login.html',{'login_form':login_form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('main')

def register_view(request):
    if request.method=="POST":
        register_form=UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user=register_form.save()
            user.refresh_from_db()
            login(request,user)
            messages.success(request,f'You are now registered as {user.username}')
            return redirect('home')
        else:
            messages.error(request,f'An error occured while you are registering')
    elif request.method=="GET":
        register_form=UserCreationForm()
    return render(request,'views/register.html',{'register_form':register_form})


@method_decorator(login_required,name="dispatch")
class ProfileView(View):
    def get(self,request):
        user_form=UserForm(instance=request.user)
        location_form=LocationForm(instance=request.user.profile.location)
        profile_form=ProfileForm(instance=request.user.profile)
        return render(request,"views/profile.html",{"user_form":user_form,"location_form":location_form,"profile_form":profile_form})

    def post(self,request):
            user_form=UserForm(request.POST,instance=request.user)
            location_form=LocationForm(request.POST,instance=request.user.profile.location)
            profile_form=ProfileForm(request.POST,instance=request.user.profile)
            if user_form.is_valid() and location_form.is_valid() and profile_form.is_valid():
                user_form.save()
                location_form.save()
                profile_form.save()
                messages.success(request,"PROFILE IS UPDATED SUCCESSFULLY")
            else:
                messages.error(request,"PROFILE IS NOT UPDATED SUCCESSFULLY")
            return render(request,"views/profile.html",{"user_form":user_form,"location_form":location_form,"profile_form":profile_form})