from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hellow Shafiullah is Here, currently we are in About Page")

def contact(request):
    return HttpResponse("Hello Shafiullah is here, Currently we are in Conntact Page")