
from django.urls import path

from . import views

urlpatterns = [


    # Store main page

    path('', views.cart_summary, name='cart-summary'),

    path('', views.cart_add, name='cart-add'),

    path('', views.cart_delete, name='cart-delete'),

    path('', views.cart_update, name='cart-update'),



]














