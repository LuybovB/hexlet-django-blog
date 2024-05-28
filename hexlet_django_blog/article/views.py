from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Article
from .forms import ArticleForm


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

    def post(self, request, tags='python'):
        # Удаление логики, связанной с формой поиска
        articles = Article.objects.all()
        context = {
            'app_name': 'hexlet_django_blog.article',
            'tags': tags,
            'articles': articles,
        }
        return render(request, self.template_name, context)


class ArticleDetailView(View):
    template_name = 'articles/article_detail.html'

    def get(self, request, article_id, tags):
        article = Article.objects.get(id=article_id)
        context = {
            'article': article,
            'tags': tags,
        }
        return render(request, self.template_name, context)


class ArticleFormEditView(View):
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})

    def post(self, request, article_id):
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})

