from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SingUp


# Create your views here.

def sing_up(request):
    form = SingUp()
    if request.method == 'POST':
        form = SingUp(request.POST)
        if form.is_valid():
            form.save()
#            username = form.cleaned_data.get('username')
#            raw_password = form.cleaned_data.get('password')
#            user = authenticate(username=username, password=raw_password)
#            login(request, user)
            return redirect('post_list')
    else:
        form = SingUp()
    context = {'form': form}
    return render(request, 'registration/sing_up.html', context)

def sing_in(request):
    if request.method == 'POST':
        None


    return render(request, 'authorization/sing_in.html')


