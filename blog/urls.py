from django.urls import path
from . views import ArticleListView, ArticleDetailView, show_tag

urlpatterns = [
    path("tag/", show_tag, name='show_tag'),
    path("articles/", ArticleListView.as_view(), name='articles'),
    path("article/<str:slug>", ArticleDetailView.as_view(), name='article_detail')
]