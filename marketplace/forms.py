from django import forms
from .models import Vehicle
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['title', 'vehicle_type', 'description', 'price', 'image']  # Use existing fields

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Replace with your custom user model if you're using one
        fields = ['username', 'email', 'password1', 'password2']