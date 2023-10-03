
from django.urls import path

from . import views

urlpatterns = [


    # Store main page

    path('cart/', views.cart, name='cart'),



]














