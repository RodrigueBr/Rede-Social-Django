from .models import Posts, Comment
from .forms import PostForm
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseForbidden
from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ProfileReport

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

def post_detail(request, id):
    post = get_object_or_404(Posts, id=id)
    comments = Comment.objects.filter(post=post)

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
    })

def add_comment(request, id):
    if request.method == 'POST':
        post = get_object_or_404(Posts, id=id)
        content = request.POST.get('content')

        Comment.objects.create(post=post, user=request.user, content=content)

        return redirect('post_detail', id=id)

    return HttpResponseForbidden("Método não permitido")

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return redirect('create_profile')

    return render(request, 'profile.html', {'profile': profile})

@login_required
def profile_view(request, username):
    profile = get_object_or_404(Profile, user__username=username)

    is_owner = request.user == profile.user

    return render(request, 'profile.html', {'profile': profile, 'is_owner': is_owner})

@login_required
def edit_profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)

    if request.user != profile.user:
        return redirect('profile', username=username)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=username)
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})


@login_required
def report_profile(request, username):
    reported_user = get_object_or_404(User, username=username)

    if reported_user == request.user:
        messages.error(request, "Você não pode reportar seu próprio perfil.")
        return redirect('profile', username=username)

    if request.method == 'POST':
        reason = request.POST.get('reason')
        if not reason.strip():
            messages.error(request, "Por favor, forneça um motivo para o report.")
            return redirect('profile', username=username)

        if ProfileReport.objects.filter(reported_by=request.user, reported_user=reported_user).exists():
            messages.warning(request, "Você já reportou este perfil.")
        else:
            ProfileReport.objects.create(
                reported_by=request.user,
                reported_user=reported_user,
                reason=reason
            )
            messages.success(request, "Perfil reportado com sucesso.")

    return redirect('profile', username=username)