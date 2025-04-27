from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('hello/', Hello.as_view(), name='hello'),
    path('task/', TaskAPIView.as_view(), name= "TaskApi" ),
    path('login/', obtain_auth_token, name = "api-login")
]
