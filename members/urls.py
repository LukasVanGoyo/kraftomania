from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name="login_page"),
    path('register', views.register, name="register"),
    path('logout', views.logout_user, name="logout"),
    path('activate/<uid64>/<token>', views.activate, name="activate"),
    path('', views.home, name="home"),
    path('profile', views.user_profile, name="user_profile")
]