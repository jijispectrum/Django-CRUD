# pets/forms.py
from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'age', 'owner_name']
