from django.urls import path
from hexlet_django_blog.article.views import ArticleListView, ArticleDetailView


urlpatterns = [
    path('', ArticleListView.as_view()),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/tags/<str:tags>/<int:article_id>/', ArticleDetailView.as_view(), name='article_detail'),
]
