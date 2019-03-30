from django import forms
from .models import UserProfile, GuestEmail
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class GuestForm(forms.Form):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class' : 'form-control','placeholder':'you@example.com', 'id':"email"}))
    name  = forms.CharField(required=True,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Your Name'}))

class RegisterForm(forms.ModelForm):
    full_name= forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Your Name*'
    }))

    email= forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Your Email*'
    }))

    username= forms.CharField(max_length=15,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Your Username*'
    }))

    phone = forms.CharField(max_length=10,widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Your Number*',
        'minlength':'10',
        'maxlength':'10'
    }))

    password= forms.CharField(widget=forms.PasswordInput(attrs={
    'class':'form-control',
    'placeholder':'Your Password*'
    }))
    password2= forms.CharField(label='Verify Password',widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Verify Password*'
    }))

    class Meta:
        model = User
        fields=('full_name', 'username','email', 'password', 'password2')

    def clean(self):
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')
        username = self.cleaned_data.get('username')

        if password2 != password:
            raise forms.ValidationError('Password should be same!')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        "class":'form-control',
        'placeholder':'Your Username'
    }))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={
        "class":'form-control',
        'placeholder':'Your Password'
    }))

    class Meta:
        model = UserProfile
        fields=('username', 'password')
