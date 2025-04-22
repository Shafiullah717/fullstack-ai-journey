from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('add_student/', add_student, name = 'add_student')
]
