from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import LoginForm, SignUpForm

# direct user to home page
def home(request):
    return render(request, 'index.html', {'user': request.user})

# direct user to menu page
def menu(request):
    return render(request, 'menu.html', {'user': request.user})

# direct user to specials page
def specials(request):
    return render(request, 'specials.html', {'user': request.user})

# direct user to cart page
def cart(request):
    return render(request, 'cart.html', {'user': request.user})

# direct user to account creation page
def account(request):
    return render(request, 'account.html', {})

# direct user to account login page
def login_page(request):
    return render(request, 'login.html', {})

# function takes cart information and displays on screen
def checkout(request):
    if request.method == 'POST':
        # Retrieve user details from the form
        first_name = request.POST.get('first_name')
        address = request.POST.get('address')

        # Process the checkout and render the checkout.html template
        return render(request, 'checkout.html', {'user': request.user, 'first_name': first_name, 'address': address})
    return render(request, 'checkout.html', {'user': request.user})

# handles user account creation
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page
    else:
        form = SignUpForm()
    return render(request, 'account.html', {'form': form})

# handles user login
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # replace 'home' with your home view name
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logs user out of current session
def logout_user(request):
    logout(request)
    return redirect('home')



