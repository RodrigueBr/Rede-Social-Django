from django.urls import path
from . import views

urlpatterns = [
    path('posts/criar', views.criar_post, name='criar_post'),
    path('posts/', views.listar_posts, name='listar_posts'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
]