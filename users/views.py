from .forms import SingUp
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
            return redirect('post_list')

    context = {}
    return render(request, 'authorization/sing_in.html', context)


def logout_user(request):
    logout(request)
    return redirect('post_list')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            #redirect('user_page')
        else:
            redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'user_page/change_password.html', context)

def user_page(request):
    if request.user.is_authenticated:
        return render(request, 'user_page/user_page.html')
    else:
        redirect('post_list')