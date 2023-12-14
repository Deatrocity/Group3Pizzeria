from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    # add any additional fields if needed
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    # add any additional fields if needed
    class Meta:
        model = CustomUser
        fields = ('username', 'password')