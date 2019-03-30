import time
from django.shortcuts import render, redirect
from .forms import AddressForm
from .models import Address
from billing.models import UserBillingProfile
from Carts.models import Cart
from Orders.models import Order
from django.utils.http import is_safe_url

def checkout_address_view(request):
    form = AddressForm(request.POST or None)
    context = {'form': form}
    next_get=request.GET.get('next')
    next_post=request.POST.get('next')
    redirect_path = next_get or next_post

    cart_obj, new_cart = Cart.objects.new_or_get(request)
    billing_profile, billing_profile_created = UserBillingProfile.objects.new_or_get(request)

    if billing_profile is not None:
        order_obj, order_obj_created =Order.objects.new_or_get(billing_profile, cart_obj)

    if form.is_valid():
        print(request.POST)
        instance = form.save(commit=False)
        billing_profile, billing_profile_created = UserBillingProfile.objects.new_or_get(request)
        if billing_profile is not None:
            instance.billing_profile = billing_profile
            instance.save()
            request.session["address_id"] = instance.id

        else:
            print("Error")

        if request.method == "POST":
            is_done = order_obj.check_done()
            print(is_done)
            if is_done:
                order_obj.mark_paid()
                print("paid")
                del request.session['cart_id']

        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            print("Error please sort it out")
            return redirect("Carts:cart_home")

    return redirect("Carts:cart_home")


def checkout_address_reuse_view(request):
    if request.user.is_authenticated():
        next_get=request.GET.get('next')
        next_post=request.POST.get('next')
        redirect_path = next_get or next_post or None
        if request.method == "POST":
            print(request.POST)
            delivery_address_id = request.POST.get("address", None)
            billing_profile, billing_profile_created = UserBillingProfile.objects.new_or_get(request)
            if billing_profile is not None:
                cart_obj, new_cart = Cart.objects.new_or_get(request)
                order_obj, order_obj_created =Order.objects.new_or_get(billing_profile, cart_obj)
            if delivery_address_id is not None:
                qs = Address.objects.filter(billing_profile=billing_profile, id=delivery_address_id)
                if qs.exists():
                    request.session["address_id"] = delivery_address_id
                if is_safe_url(redirect_path, request.get_host()):
                    return redirect(redirect_path)
    return redirect("Carts:cart_home")
