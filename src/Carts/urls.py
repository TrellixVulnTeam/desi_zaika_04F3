from django.conf.urls import url, include
from .views import cart_home, cart_update, cart_checkout


urlpatterns = [
    url(r'^cart/$',cart_home, name="cart_home"),
    url(r'^cart/update/$',cart_update, name="cart_update"),
    url(r'^cart/checkout/$',cart_checkout, name="cart_checkout"),
]
