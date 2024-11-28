from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_post, name='criar_post'),
    path('criar-post/', views.criar_post, name='criar_post'),
    path('posts/', views.listar_posts, name='listagem_posts'),
]