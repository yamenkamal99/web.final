from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_subject, name='add_subject'),
    path('edit/<int:pk>/', views.edit_subject, name='edit_subject'),
    path('delete/<int:pk>/', views.delete_subject, name='delete_subject'),
]