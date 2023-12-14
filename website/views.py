from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import LoginForm, SignUpForm


def home(request):
    return render(request, 'index.html', {'user': request.user})

def menu(request):
    return render(request, 'menu.html', {'user': request.user})

def specials(request):
    return render(request, 'specials.html', {'user': request.user})

def cart(request):
    return render(request, 'cart.html', {'user': request.user})

def account(request):
    return render(request, 'account.html', {})

def login_page(request):
    return render(request, 'login.html', {})

def checkout(request):
    return render(request, 'checkout.html', {'user': request.user})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("account created success")
            return redirect('home')  # Redirect to the home page or any desired page
        else:
            print("account creation fail")
    else:
        form = SignUpForm()
    return render(request, 'account.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("login success")
            return redirect('home')  # replace 'home' with your home view name
        else:
            print("login fail")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')



