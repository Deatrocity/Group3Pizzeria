from django.urls import path, include
from . import views
from .views import create_account, login_page, login_view

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('specials/', views.specials, name="specials"),
    path('cart/', views.cart, name="cart"),
    path('account/', views.account, name="account"),
    path('login/', views.login_page, name="loginpage"),
    path('loginresult/', views.login_view, name='loginresult'),
    path('checkout/', views.checkout, name="checkout"),
    path('create_account/', create_account, name='create_account'),
]