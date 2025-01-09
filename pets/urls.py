# pets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_pet, name='add_pet'),
    path('list/', views.pet_list, name='pet_list'),  # Assuming this view shows a list of pets
]
