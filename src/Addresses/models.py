from django.db import models
from billing.models import UserBillingProfile

class Address(models.Model):
    billing_profile=models.ForeignKey(UserBillingProfile)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150, null=True, blank=True)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    state =models.CharField(max_length=50)

    def __str__(self):
        return str(self.billing_profile)
