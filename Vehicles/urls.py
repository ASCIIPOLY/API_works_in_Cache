from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.redirectpage, name="redirectpage"),
    path('listpage/', views.listPage, name="listPage"),
    path('detailpage/<int:pk>/', views.vehicle_model_detail, name="vehicle_model_detail"),  

] 