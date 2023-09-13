from django.shortcuts import render
from . models import Article, Tag, Comment
from django.views.generic import ListView, DetailView
from .serializers import ArticleSerializer, CommentSerializer, TagSerializer, LikeSerializer, CategorySerializer
from rest_framework import generics



class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Article.objects.filter(user=user)

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'


class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer   


class UserArticles(generics.ListAPIView):
    serializer_class = ArticleSerializer

def show_tag(request):
    articles = Article.objects.filter(tags__name = 'piwo')
    return render(request , 'blog/show_tag.html', {'articles': articles})