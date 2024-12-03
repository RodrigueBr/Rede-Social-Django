from django.urls import path
from . import views
from .views import logout_view


urlpatterns = [
    path('criar-post/', views.criar_post, name='criar_post'),
    path('posts/', views.listar_posts, name='listar_posts'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/<int:id>/comentar/', views.add_comment, name='add_comment'),
    path('perfil/', views.profile, name='profile'),
    path('editar-perfil/<str:username>/', views.edit_profile, name='edit_profile'),
    path('perfil/<str:username>/', views.profile_view, name='profile'),
    path('report/<str:username>/', views.report_profile, name='report_profile'),
]