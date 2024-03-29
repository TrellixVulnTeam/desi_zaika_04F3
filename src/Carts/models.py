from decimal import Decimal
from django.db import models
from Products.models import Product
from django.conf import settings
from django.db.models.signals import m2m_changed, pre_save

User = settings.AUTH_USER_MODEL

class CartManger(models.Manager):
    def new_or_get(self, request):
        cart_id=request.session.get('cart_id', None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count()==1 and qs.exists:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj =True
            request.session['cart_id']= cart_obj.id
        return cart_obj , new_obj

    def new(self, user=None):
        user_obj=None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user            =models.ForeignKey(User, null=True, blank=True)
    products        =models.ManyToManyField(Product, blank=True)
    subtotal        =models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total           =models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    updated         =models.DateTimeField(auto_now=True)
    timestamp       =models.DateTimeField(auto_now_add=True)

    objects = CartManger()

    def __str__(self):
        return str(self.timestamp)



def m2m_changed_cart_receiver(sender, instance, action,*args, **kwargs):
    if action == 'post_add' or action=='post_remove' or  action == 'post_clear':
        products = instance.products.all()
        total_price = 0
        for product in products:
            total_price += product.price
        if instance.subtotal != total_price:
            instance.subtotal = total_price
            instance.save()


m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)


def pre_save_cart_receiver(sender, instance, *args,**kwargs):
    if instance.subtotal > 0:
        instance.total = Decimal(instance.subtotal) * Decimal(1.12)
    else:
        instance.total = 0

pre_save.connect(pre_save_cart_receiver, sender=Cart)
