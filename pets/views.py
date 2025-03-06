from django.shortcuts import render

# Create your views here.
# pets/views.py
from django.shortcuts import render, redirect,get_object_or_404
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


def edit_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()  # Save the updated pet record
            return redirect('pet_list')
    else:
        form = PetForm(instance=pet)  # Pre-fill the form with the existing pet data
    
    return render(request, 'edit_pet.html', {'form': form, 'pet': pet})



def delete_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        pet.delete()  # Delete the pet record
        return redirect('pet_list')
    
    return render(request, 'delete_pet.html', {'pet': pet})
