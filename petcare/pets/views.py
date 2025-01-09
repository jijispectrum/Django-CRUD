from django.shortcuts import render

# Create your views here.
# pets/views.py
from django.shortcuts import render, redirect
from .forms import PetForm

def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new pet record
            return redirect('pet_list')  # Redirect to the pet list page after saving
    else:
        form = PetForm()  # Display an empty form for GET requests
    
    return render(request, 'add_pet.html', {'form': form})


# pets/views.py
from django.shortcuts import render
from .models import Pet

def pet_list(request):
    pets = Pet.objects.all()  # Get all pets from the database
    return render(request, 'pet_list.html', {'pets': pets})
