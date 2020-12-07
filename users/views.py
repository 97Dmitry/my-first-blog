from .forms import SingUp
from blog.models import Post
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

# Create your views here.

def sing_up(request):
    if request.method == 'POST':
        form = SingUp(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            messages.success(request, 'Вы успешно зарегестрировались')
            return redirect('post_list')
    else:

        form = SingUp()
    context = {'form': form}
    return render(request, 'registration/sing_up.html', context)


def sing_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Вы успешно авторизовались под именем {username}')
            return redirect('post_list')

    context = {}
    return render(request, 'authorization/sing_in.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, 'Вы вышли из аккаунта')
    return redirect('post_list')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пароль успешно изменен')
            update_session_auth_hash(request, form.user)
        else:
            redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'user_page/change_password.html', context)

def user_page(request):
    if request.user.is_authenticated:
        user_posts = Post.objects.filter(author=request.user)
        content = {'user_posts': user_posts}
        return render(request, 'user_page/user_page.html', content)
    else:
        redirect('post_list')