from django.shortcuts import render
from django.forms import ValidationError
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib import auth
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser, UserProfile
from .serializers import CreateUserSerializer, ProfileSerializer, MyTokenObtainPairSerializer, UserSerializer



def home(request):
    return render(request, 'base.html')


@method_decorator(csrf_protect, name='dispatch')



class UserView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
       


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        data=self.request.data
        serializer = CreateUserSerializer(data=data)

        password = data['password']
        password2 = data['password2']
        username = data['username']
        email = data['email']

        is_email = CustomUser.objects.filter(email=email).first()

        if is_email:
             return Response({"message": "Podane adres email jest zajęty."}, status=status.HTTP_400_BAD_REQUEST)
            
        
        if password != password2:
            return Response({"message": "Podane hasła nie są identyczne."}, status=status.HTTP_400_BAD_REQUEST)
        
        if len(password) < 8:
            return Response({"message":"Hasło musi zawierać minimum 8 znaków."}, status=status.HTTP_400_BAD_REQUEST)
        
        if len(username) < 3:
            return Response({"message":"Nazwa użytkownika musi zawierać minimum 3 znaki."}, status=status.HTTP_400_BAD_REQUEST)


        if not serializer.is_valid():
            return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.create(serializer.validated_data)
        user = CreateUserSerializer(user)
       
        return Response(user.data, status=status.HTTP_201_CREATED)
    
  
        
class UserProfile(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()
        

@method_decorator(ensure_csrf_cookie, name="dispatch")
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({'success': 'CSRF cookie set'})
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer