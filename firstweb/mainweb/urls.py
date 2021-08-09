# 2
from django.urls import path
from . import views

urlpatterns = [
    path('sapa/<str:nama>/', views.sapa),
    path('count/<int:angka>/', views.count),
    path('hmlcoba/', views.htmlcoba),
    path('second/', views.second_page),
    path('', views.landing_page),
]
