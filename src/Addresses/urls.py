from django.conf.urls import url
from .views import checkout_address_view ,checkout_address_reuse_view

urlpatterns = [

    url(r'^checkout/$', checkout_address_view, name="checkout_address_view"),
    url(r'^checkout/reuse/$', checkout_address_reuse_view, name="checkout_address_reuse_view"),
]
