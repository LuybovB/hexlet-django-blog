from django.shortcuts import render
from django.views import View
from .models import Article


class ArticleListView(View):
    template_name = 'articles/index.html'

    def get(self, request, tags='python'):
        articles = Article.objects.all()
        context = {
            'app_name': 'hexlet_django_blog.article',
            'tags': tags,
            'articles': articles,
        }
        return render(request, self.template_name, context)


class ArticleDetailView(View):
    template_name = 'articles/article_detail.html'

    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        context = {
            'article': article,
        }
        return render(request, self.template_name, context)
