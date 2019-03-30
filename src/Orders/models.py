import math
from django.shortcuts import redirect
from django.db import models
from Carts.models import Cart
from billing.models import UserBillingProfile
from django.db.models.signals import pre_save,post_save
from Addresses.models import Address
from ecommerce.utils import order_id_gen

class OrderManager(models.Manager):
    def new_or_get(self, billing_profile, cart_obj):
        created=False
        qs = self.get_queryset().filter(billing_profile=billing_profile, cart=cart_obj, status="created", active=True)
        if qs.count()==1:
            obj = qs.first()
        else:
            obj = self.model.objects.create(billing_profile=billing_profile,cart=cart_obj)
            created=True
        return obj, created

class Order(models.Model):
    order_status_choices=(
        ('created', 'Created'),
        ('in progress', 'In Progress'),
        ('delivered', 'Delivered'),
        ('refunded', 'Refunded'),
        #('paid', 'Paid')
    )
    billing_profile      = models.ForeignKey(UserBillingProfile, null=True, blank=True)
    delivery_address     = models.ForeignKey(Address,null=True, blank=True)
    order_id             = models.CharField(max_length=150, blank=True)
    # email = models.EmailField()
    # phone = models.PositiveIntegerField()
    cart                 = models.ForeignKey(Cart)
    status               = models.CharField(max_length=100, default='created', choices=order_status_choices)
    created              = models.DateTimeField(auto_now_add=True)
    updated              = models.DateTimeField(auto_now=True)
    paid                 = models.BooleanField(default=False)
    # tax                  = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)
    delivery_charges     = models.DecimalField(max_digits=5, decimal_places=2, default=20.00)
    order_total          = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    active               = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.order_id

    objects = OrderManager()

    def updatetotal(self):
        cart_total = self.cart.total
        tax_total = 10  * cart_total/100
        new_total = math.fsum([cart_total, tax_total])
        if(new_total>300):
            self.delivery_charges = 0
        new_total = new_total + self.delivery_charges
        formatted_total = format(new_total, '.2f')
        self.order_total =formatted_total
        self.save()
        return formatted_total

    def check_done(self):
        billing_profile = self.billing_profile
        delivery_address = self.delivery_address
        order_total = self.order_total
        if billing_profile and  delivery_address and order_total > 0:
            return True
        else:
            return False

    def mark_paid(self):
        if self.check_done():
            self.paid = True
            self.save()
            return self.paid

def create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = order_id_gen(instance)
    qs = Order.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile, active=True)
    if qs.exists():
        qs.update(active=False)

pre_save.connect(create_order_id, sender=Order)

def ps_cart_total(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count()==1:
            order_obj = qs.first()
            order_obj.updatetotal()

post_save.connect(ps_cart_total, sender=Cart)

def ps_order(sender,instance, created, *args, **kwargs):
    if created:
        instance.updatetotal()
post_save.connect(ps_order, sender=Order)
