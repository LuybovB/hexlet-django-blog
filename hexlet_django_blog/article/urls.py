from django.urls import path
from hexlet_django_blog.article.views import ArticleListView, ArticleDetailView, ArticleFormEditView


urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_index'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('<int:article_id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    path('tags/<str:tags>/<int:article_id>/', ArticleDetailView.as_view(), name='article_detail'),
]
