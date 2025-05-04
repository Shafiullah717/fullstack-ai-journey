from django.urls import path
from .views import *

urlpatterns = [
    path('student/', StudentApi.as_view(), name='student_api'),
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('hello/', Hello.as_view(), name='hello_world'),
]
