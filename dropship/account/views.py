from django.shortcuts import render


#from django.shortcuts import get_object_or_404


def login(request):

    return render(request, 'login.html')

def register(request):

    return render(request, 'register.html')