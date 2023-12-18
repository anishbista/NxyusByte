from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("display_product")

    else:
        form = ProductForm()
    return render(request, "add_product.html", {"form": form})


def display_product(request):
    product = Product.objects.all()
    category = Category.objects.prefetch_related("product").all()
    for c in category:
        print(c.product)
    return render(request, "index.html", {"products": product, "category": category})


def product_detail(request, pk):
    product = Product.objects.select_related("category").get(pk=pk)
    return render(request, "product_detail.html", {"product": product})


def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(request.POST, request.FILES, instance=product)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("display_product")
    return render(request, "update_product.html", {"form": form, "product": product})


def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("display_product")
    return render(request, "delete_product.html", {"product": product})
