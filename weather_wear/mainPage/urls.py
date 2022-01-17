from django.urls import path
from .views import *

app_name = "mainPage"
urlpatterns = [
    path('', mainpage , name="mainpage"),
    path('today/', today, name="today"),
]