from django import forms
from .import models

class CreateProduct(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=[ 'name', 'quantity', 'price', 'description', 'thumb',]