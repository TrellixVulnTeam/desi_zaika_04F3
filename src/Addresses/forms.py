from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    address_line_1 = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter Delivery Address',
    }))
    address_line_2= forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter nearby landmark',
    }))
    city=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter Your city',
    }))
    state=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter Your state',
    }))
    postal_code=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter Pincode',
    }))
    class Meta:
        model = Address
        fields = (
            '__all__'
        )
        exclude=('billing_profile',)
