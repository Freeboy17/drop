
from django.urls import path

from . import views

urlpatterns = [


    # Store main page

    path('', views.store, name='store'),
    path('home/', views.home, name='home'),
    path('product/', views.product_page, name='prod'),



]














