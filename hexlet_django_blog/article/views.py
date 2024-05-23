from django.shortcuts import render


def index(request):
    context = {
        'app_name': 'hexlet_django_blog.article',  # Здесь можно передать динамическое значение
       }
    return render(request, 'articles/index.html', context)