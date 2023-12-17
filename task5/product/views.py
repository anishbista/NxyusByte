from django.shortcuts import render
from .models import Product
from .forms import ProductForm


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ProductForm()
    return render(request, "add_product.html", {"form": form})
