from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SingUp


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
