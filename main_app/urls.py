from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/<int:dog_id>/add_walking/', views.add_walking, name='add_walking'),
    path('dogs/<int:dog_id>/unused_toy/<int:toy_id>/', views.unused_toy, name="unused_toy"),
    path('dogs/<int:dog_id>/dogs_toy/<int:toy_id>/', views.dogs_toy, name="dogs_toy"),
    path('dogs/new/', views.add_dog, name='add_dog'),
    path('dogs/<int:dog_id>/edit/', views.edit_dog, name='edit_dog'),
    path('dogs/<int:dog_id>/delete/', views.delete_dog, name='delete_dog'),
    path('accounts/signup', views.signup, name='signup')
]