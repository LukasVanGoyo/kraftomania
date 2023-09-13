from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [ 
    path('', views.home, name="home"),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', views.RegisterView.as_view(), name="register"),
    path('csrf_token/', views.GetCSRFToken.as_view(), name="csrf_token"),
    path('profile/', views.UserProfile.as_view(), name="user_profile"),
    path('users/', views.UserView.as_view(), name='users')
    
]