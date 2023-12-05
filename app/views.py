from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
import sqlite3
connect = sqlite3.connect("../db.sqlite3")
cursor = connect.cursor()

def index(request):
    return render(request, 'index.html')


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def contact(request):
    return render(request, 'contact.html')

def viewProduct(request, id):
    products = Product.objects.all()
    for product in products:
        if product.id == id:
            return render(request, 'product.view.html', {'product': product})