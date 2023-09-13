from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from members.models import UserProfile, CustomUser



class Category(models.Model):
    CATEGORY = [
       ('Kiszonki', 'Kiszonki'),
       ('Piwo', 'Piwo'),
       ('Konfitury', 'Konfitury')
    ]
    name = models.CharField(
        choices = CATEGORY
    )
    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(
        max_length=50
    )
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(
        max_length= 50,
        
    )
    body = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='articles')
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
    slug = models.SlugField(blank=True, unique=True)
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)  
    
    def __str__(self):
        return self.title
    
    
    def short_desc(self):
        desc = self.body
        short = desc[0:140]
        return short + '...'
    


class Like(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    
    

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    added_at = models.DateTimeField(
        auto_now_add=True,
        null = True
    )

    def __str__(self):
        return self.text