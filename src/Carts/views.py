from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Cart
from Products.models import Product
from Orders.models import Order
from billing.models import UserBillingProfile
from registeration.models import GuestEmail
from registeration.forms import RegisterForm, LoginForm, GuestForm
from Addresses.forms import AddressForm
from Addresses.models import Address

def cart_home(request):
    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    cart_obj, new_cart = Cart.objects.new_or_get(request)
    order_obj = None
    address_id = request.session.get("address_id", None)
    billing_profile, billing_profile_created = UserBillingProfile.objects.new_or_get(request)
    address_qs = None
    for key, value in request.session.items(): print('{} => {}'.format(key, value))
    if billing_profile is not None:
        address_qs = Address.objects.filter(billing_profile=billing_profile)
        order_obj, order_obj_created =Order.objects.new_or_get(billing_profile, cart_obj)
        if address_id:
            order_obj.delivery_address = Address.objects.get(id=address_id)
            request.session['cart_product_count'] = 0
            del request.session['address_id']
            order_obj.save()

    context={
    "cart":cart_obj,
    "login_form":login_form,
    "guest_form":guest_form,
    'order':order_obj,
    "billing_profile":billing_profile,
    "address_form":address_form,
    "address_qs":address_qs
    }
    return render(request, "Carts/cart-home.html", context)


def cart_update(request):
    product_id=request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Http404("Product does not exist!")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
            product_added = False
        else:
            cart_obj.products.add(product_obj)
            product_added = True

        request.session['cart_product_count']= cart_obj.products.count()
        if request.is_ajax():
            print("Ajax")
            json_data = {
                "added": product_added,
                "removed": not product_added,
                "cartProductCount": cart_obj.products.count()
            }
            return JsonResponse(json_data)
    return redirect("Carts:cart_home")


def cart_checkout(request):
    return render(request, "Carts/success.html", {})
