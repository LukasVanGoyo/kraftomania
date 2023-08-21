from django.contrib import admin
from .models import UserProfile, CustomUser

admin.site.register(UserProfile)
# Register your models here.
admin.site.register(CustomUser)