from django.urls import path
from hexlet_django_blog.article.views import CustomIndexView


urlpatterns = [
    path('', CustomIndexView.as_view()),
]
