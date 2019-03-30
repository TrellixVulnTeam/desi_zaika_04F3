from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
# Create your models here.

def validate_phone_length(value):
    if(value.length>10):
        raise ValidationError("Not a valid phone number");

class UserProfile(models.Model):
    user        =models.OneToOneField(User, on_delete=models.CASCADE)
    phone       =models.PositiveIntegerField(blank=False, unique=True, null=False, validators=[])
    timestamp   =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class GuestEmail(models.Model):
    email       =models.EmailField()
    name        =models.CharField(max_length=50)
    timestamp   =models.DateTimeField(auto_now_add=True)
    updated     =models.DateTimeField(auto_now=True)
    active      =models.BooleanField(default=True)

    def __str__(self):
        return self.email
