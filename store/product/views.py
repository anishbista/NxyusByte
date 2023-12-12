from django.shortcuts import render
from .utils import get_products


def product_list(request):
    product = get_products()
    return render(request, "product.html", {"product": product})
