from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import create_an_account, Register


class RegistForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Register
        fields = "__all__"


class CreateForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = create_an_account
        fields = ['username', 'email', 'Mobile', 'address', 'PIN', 'city', 'state', 'account_type', 'initial_balance',
                  'password']
