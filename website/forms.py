from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserAccount


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = UserAccount
#         fields = ['username', 'password']