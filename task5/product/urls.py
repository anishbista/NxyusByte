from django.urls import path
from . import views

urlpatterns = [
    path("", views.display_product, name="display_product"),
    path("add/", views.add_product, name="add_product"),
    path("detail/<int:pk>", views.product_detail, name="product_detail"),
    path("product/<int:pk>/update", views.update_product, name="update_product"),
    path("product/<int:pk>/delete", views.delete_product, name="delete_product"),
]
