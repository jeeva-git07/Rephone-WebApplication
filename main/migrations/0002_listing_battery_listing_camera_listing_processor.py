# Generated by Django 5.1.5 on 2025-05-14 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='battery',
            field=models.CharField(default='0 mah', max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='camera',
            field=models.CharField(default='0 Mp', max_length=30),
        ),
        migrations.AddField(
            model_name='listing',
            name='processor',
            field=models.CharField(default='Enter Processor here', max_length=24),
        ),
    ]
