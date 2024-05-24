from django.shortcuts import render
from django.views import View


class CustomIndexView(View):
    template_name = 'articles/index.html'

    def get_context_data(self, tags=None, article_id=None):  # Добавляем параметры tags и article_id
        context = {
            'app_name': 'hexlet_django_blog.article',
            'tags': tags,  # Пример добавления tags в контекст
            'article_id': article_id,  # Пример добавления article_id в контекст
        }
        return context

    def get(self, request, tags=None, article_id=0):
        tags = tags if tags else 'python'
        article_id = article_id if article_id else 42
        context = self.get_context_data(tags, article_id)
        return render(request, self.template_name, context)


