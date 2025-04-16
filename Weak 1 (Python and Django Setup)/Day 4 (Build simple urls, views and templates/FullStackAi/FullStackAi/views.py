from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hellow Shafiullah is here, you are on home page")
    return render(request, 'home.html')
def about(request):
    # return HttpResponse("hello Shafiullah is here, you are on about page")
    return render(request, 'about.html')