from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserAccountForm, LoginForm
from django.http import HttpResponse
from .models import UserAccount



def home(request):
    return render(request, 'index.html', {})

def menu(request):
    return render(request, 'menu.html', {})

def specials(request):
    return render(request, 'specials.html', {})

def cart(request):
    return render(request, 'cart.html', {})

def account(request):
    return render(request, 'account.html', {})

# def login_page(request):
#     return render(request, 'login.html', {})

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Handle form submission and authentication if needed
            pass
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def checkout(request):
    return render(request, 'checkout.html', {})

def create_account(request):
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
        else:
            messages.error(request, 'Account creation failed. Please check the form data.')
    else:
        form = UserAccountForm()

    return render(request, 'account.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate using your UserAccount model
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            # return redirect('home')  # Redirect to the home page or any desired page
        else:
            messages.error(request, 'Login failed, check username and password.')

    return render(request, 'login.html')



