from django.urls import path
from . views import ArticleListView, ArticleDetailView, CommentListView



urlpatterns = [
    
    path("articles/", ArticleListView.as_view(), name='articles'),
    path("article/<str:slug>", ArticleDetailView.as_view(), name='article_detail'),
    path("comments/", CommentListView.as_view(), name='comments'),
    ]