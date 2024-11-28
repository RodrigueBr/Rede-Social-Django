from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostForm


def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listagem_posts')
    else:
        form = PostForm()
    return render(request, 'criar_post.html', {'form': form})


def listar_posts(request):
    posts = Posts.objects.all()
    return render(request, 'listar_posts.html', {'posts': posts})

