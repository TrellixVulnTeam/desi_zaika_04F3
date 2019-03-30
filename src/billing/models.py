from django.db import models
from django.contrib.auth.models import User
from registeration.models import GuestEmail
from django.db.models.signals import post_save

class UserBillingProfileManager(models.Manager):
    def new_or_get(self, request):
        user = request.user
        guest_email_id = request.session.get('guest_email_id')
        created = False
        obj=None
        if user.is_authenticated():
            obj, created = UserBillingProfile.objects.get_or_create(user=user, email=user.email)

        elif guest_email_id is not None:
            guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
            obj, created = UserBillingProfile.objects.get_or_create(email=guest_email_obj.email)

        else:
            pass
        return obj, created

class UserBillingProfile(models.Model):
    user        =models.OneToOneField(User, blank=True, null=True)
    email       =models.EmailField()
    # phone       =models.PositiveIntegerField()
    timestamp   =models.DateTimeField(auto_now_add=True)
    updated     =models.DateTimeField(auto_now=True)
    active      =models.BooleanField(default=True)

    objects = UserBillingProfileManager()

    def __str__(self):
        return self.email

def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        UserBillingProfile.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(user_created_receiver, sender=User)
