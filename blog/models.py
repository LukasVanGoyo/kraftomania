from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(
        max_length= 250,
        
    )
    body = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    added_at = models.DateTimeField(
        auto_now_add=True,
        null = True
    )
    image = models.ImageField(
        blank=True
    )
    likes = models.IntegerField(
        default = 0,
        blank=True
    )
    votes= models.IntegerField(
        default=0,
        blank=True
    )
    rating= models.BigIntegerField(
        default=0,
        blank=True
    )
    

    def __str__(self):
        return self.title
    