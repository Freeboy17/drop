
from django.urls import path

from . import views

urlpatterns = [


    # Store main page

    path('about/', views.about, name='about'),



]














