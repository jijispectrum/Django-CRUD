# pets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_pet, name='add_pet'),
    path('list/', views.pet_list, name='pet_list'),
    path('edit/<int:pk>/', views.edit_pet, name='edit_pet'),  # Edit a pet
    path('delete/<int:pk>/', views.delete_pet, name='delete_pet'),  # Assuming this view shows a list of pets
]
