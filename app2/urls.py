from app2.views import *
from django.urls import path
app_name='s2'

urlpatterns=[
    path('rk/',rk,name='rk'),
]