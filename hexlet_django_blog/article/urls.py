from django.urls import path
from hexlet_django_blog.article.views import CustomIndexView


urlpatterns = [
    path('', CustomIndexView.as_view()),
    path('tags/<str:tags>/<int:article_id>/', CustomIndexView.as_view()),  # Маршрут с параметрами tags и article_id

]
