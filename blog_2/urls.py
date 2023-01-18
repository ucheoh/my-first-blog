from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog2-home'),
    path('about/', views.about, name='blog2-about'),
]
