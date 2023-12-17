from django.urls import path
from . import views

urlpatterns = [
    path("", views.display_product, name="display_product"),
    path("add/", views.add_product, name="add_product"),
]
