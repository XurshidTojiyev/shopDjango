from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name=""),
    path('products/', products, name="products"),
    path('contact/', contact, name="contact"),
    path('products/<int:id>/', viewProduct)
]
