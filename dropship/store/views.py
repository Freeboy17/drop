from django.shortcuts import render

from . models import Category, Product

from django.shortcuts import get_object_or_404


def store(request):

    all_products = Product.objects.all()

    context = {'my_products':all_products}

    return render(request, 'store.html', context)

def home(request):

    all_products = Product.objects.all()

    return render(request, 'home.html')

def product_page(request):

    all_products = Product.objects.all()
    print(Product.objects.all())

    return render(request, 'product-page.html')
