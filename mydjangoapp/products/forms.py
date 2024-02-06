from django import forms
from .import models

class CreateProduct(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=[ 'name', 'quantity', 'price', 'description', 'thumb',]

class CheckoutForm(forms.Form):
    card_number = forms.CharField(label='Card Number', max_length=16, required=False)
    expiration_date = forms.DateField(label='Expiration Date', widget=forms.TextInput(attrs={'placeholder': 'MM/YY'}), required=False)
    cvv = forms.CharField(label='CVV', max_length=3, required=False)
    payment_method = forms.ChoiceField(choices=[('card', 'Credit Card'), ('cash', 'Cash')], widget=forms.RadioSelect)
    delivery_option = forms.ChoiceField(choices=[('pickup', 'Pickup'), ('delivery', 'Home Delivery')], widget=forms.RadioSelect)
    delivery_address = forms.CharField(label='Delivery Address', required=False, widget=forms.Textarea(attrs={'rows': 3}))