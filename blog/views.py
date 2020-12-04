from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import PostForm
from .models import Post, Rubric


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    # posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    count_posts = Post.objects.values('title').aggregate(Count('title'))
    context = {'posts': posts, 'count_posts': count_posts.get('title__count')}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def about_blogs(request):
    return render(request, 'blog/about_blogs.html')


def post_new(request):
    if not request.user.is_authenticated:
        return redirect('sing_in')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid() and form.cleaned_data():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    """Редактирование существующей записи"""
    if not request.user.is_authenticated:  # Проверка авторизации
        return redirect('sing_in')
    author_name = Post.objects.get(pk=pk).author  # Из базы данных получаем вызываемую запись и выбираем автора
    if request.user.username != author_name.username:  # Если человек не является автором - редакция запрещена
        return redirect('post_list')
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":  # Если пользователь отправляет данные
        form = PostForm(request.POST, instance=post)  # В Post - форму становится возможным внести изменения и сохранить
        if form.is_valid() and form.cleaned_data():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})


def by_rubric(request, rubric_id):
    """ Получив rubric_id из urls, мы в переменную posts получаем
        все посты с данным тегом. В current_rubric мы получили название
        название тега. Затем всё это выводится в цикле for в HTML
        файле by_rubric.html
    """
    posts = Post.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    count_posts = len(posts)
    context = {'posts': posts, 'rubrics': rubrics, 'current_rubric': current_rubric,
               'count_posts': count_posts}

    return render(request, 'blog/by_rubric.html', context)


def delete_post(request, pk):
    if not request.user.is_authenticated:  # Проверка авторизации
        return redirect('sing_in')
    author_name = Post.objects.get(pk=pk).author  # Из базы данных получаем вызываемую запись и выбираем автора
    if request.user.username != author_name.username:  # Если человек не является автором - удаление запрещено
        return redirect('post_list')
    # if request.method == "POST":
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_list')


def home(request):
    return redirect('post_list')
