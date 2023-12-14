from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# handles account creation form
class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

# hands account login form
class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')