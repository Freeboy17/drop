from django.shortcuts import render


#from django.shortcuts import get_object_or_404


def about(request):

    return render(request, 'about.html')

