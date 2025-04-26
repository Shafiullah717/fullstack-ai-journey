from django.urls import path
from .views import *

urlpatterns = [
    path('student/', StudentApi.as_view(), name='student_api'),
    path('hello/', Hello.as_view(), name='hello_api'),
]
