from cProfile import label
from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(max_length=64, label="Login")
    password = forms.CharField(label="Password", max_length=128, widget=forms.PasswordInput)

