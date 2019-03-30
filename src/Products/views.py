from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import ListView

from .models import Product
from Carts.models import Cart

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "Products/ProductList.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        request = self.request
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context['cart']= cart_obj
        return context
