from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="", widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
    password = forms.CharField(max_length=128, label="", widget=forms.PasswordInput(attrs={'placeholder': "Mot de passe"}))

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=150, label="", widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
    password1 = forms.CharField(max_length=128, label="", widget=forms.PasswordInput(attrs={"placeholder": "Mot de passe"}))
    password2 = forms.CharField(max_length=128, label="", widget=forms.PasswordInput(attrs={"placeholder": "Confirmer mot de passe"}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        help_texts = {"username": None}