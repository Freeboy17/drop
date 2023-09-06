
from django.urls import path

from . import views

urlpatterns = [


    # Store main page

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),




]














