from django.urls import path, include
from . import views
from .views import login_page, signup, user_login, logout_user

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('specials/', views.specials, name="specials"),
    path('cart/', views.cart, name="cart"),
    path('account/', views.account, name="account"),
    path('loginpage/', views.login_page, name="loginpage"),
    path('checkout/', views.checkout, name="checkout"),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', logout_user, name='logout'),
]