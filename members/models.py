from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length = 50,
        unique=True,
        error_messages={
            'unique':'Podana nazwa użytkownika jest już zajęta!',
            'max_length': 'Nazwa użytkownika może zawierać maksymalnie 50 znaków.'
        }
    )
    email = models.EmailField(
        max_length = 256,
        unique=True,
        error_messages={
            'unique':'Podany adres email jest już zajęty!',
            'max_length': 'Podany adres email jest za długi.'
        }

    )

    is_active = models.BooleanField(
        default=False,
    )

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    


class UserProfile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=CustomUser)
