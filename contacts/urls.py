from django.urls import path
from . import views

urlpatterns = [
    path('inquiry/', views.inquiry, name='inquiry'),
    path('inquiry_short/', views.inquiry_short, name='inquiry_short'),
]