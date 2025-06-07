def user_listing_path(instance,filename):
    return "user{0}/filters/{1}".format(instance.seller.user.id,filename)