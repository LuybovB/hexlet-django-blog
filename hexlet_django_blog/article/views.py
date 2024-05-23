from django.shortcuts import render
from django.views import View


class CustomIndexView(View):
    template_name = 'articles/index.html'

    def get_context_data(self):
        context = {
            'app_name': 'hexlet_django_blog.article',  # Здесь можно передать динамическое значение
        }
        return context

    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)