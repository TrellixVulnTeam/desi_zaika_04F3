from django.contrib import admin
from django.contrib import admin
from .models import UserProfile, GuestEmail
# Register your models here.

admin.site.register(UserProfile)
#admin.site.register(UserBillingProfile)
admin.site.register(GuestEmail)
