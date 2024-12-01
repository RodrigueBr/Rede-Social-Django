from .models import Posts
from .forms import PostForm
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect


def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('listar_posts')
    else:
        form = PostForm()
    return render(request, 'criar_post.html', {'form': form})


def listar_posts(request):
    posts = Posts.objects.all()
    return render(request, 'listar_posts.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Usuário registrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao registrar usuário. Verifique os campos.')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'login.html')

    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('home')