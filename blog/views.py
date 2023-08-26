from django.shortcuts import render
from . models import Article, Tag
from django.views.generic import ListView, DetailView

class ArticleListView(ListView):
    model = Article

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'



def show_tag(request):
    articles = Article.objects.filter(tags__name = 'piwo')
    return render(request , 'blog/show_tag.html', {'articles': articles})