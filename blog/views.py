from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import PostForm, CommentsForm, RatingForm
from .models import Post, Rubric, ValueRatingPost
from .control_functions import can_new_post, edit_post


def post_list(request):
    posts = Post.objects.all()
    tags = Rubric.objects.all()
    # posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    count_posts = Post.objects.values('title').aggregate(Count('title'))
    paginator = Paginator(posts, 2)  # делим все полученные посты по 2
    # page_num = request.GET.get('page', 1) получаем из строки запроса параметр page, если его нет считаем что равен 1
    # другой способ получения параметра
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)

    # Логика для отображения предыдущей и следующей страницы
    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''
    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''
    context = {
        'page': page,
        'prev_url': prev_url,
        'next_url': next_url,
        'count_posts': count_posts.get('title__count'),
        'tags': tags
    }
    return render(request, 'blog/post_list.html', context)


# class ContactList(ListView): Пагинация встроенна в ListView
#     paginate_by = 2
#     model = Post


def post_detail(request, pk):
    form = CommentsForm()
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()  # Вывод всех комментариев поста
    # Сумма рейтинга
    rating_voted = ValueRatingPost.avg_values_rating(pk)
    # Создание комментария
    if request.method == "POST":
        if request.user.is_anonymous:
            messages.info(request, 'Авторизуйтесь, что бы добавить комментарий')
        else:
            form = CommentsForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = Post.objects.get(pk=pk)
                comment.name = request.user
                comment.save()
                messages.success(request, 'Комментарий успешно добавлен')
                return redirect('post_detail', pk=pk)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'current_pk': pk,
        'rating': rating_voted.get('avg'),
        'voted': rating_voted.get('voted')
    }
    return render(request, 'blog/post_detail.html', context)


def about_blogs(request):
    return render(request, 'blog/about_blogs.html')


def post_new(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Что бы создать новую запись, вы должны быть авторизованны')
        return redirect('sing_in')
    if can_new_post(request) == 1:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)  # commit равный False указывает на то, что форма готова к сохранению,
                # но в нее нужно еще внести изменения и сохранение произойдет после повторного вызова метода save()
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                messages.success(request, 'Пост успешно создан')
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        context = {
            'form': form
        }
        return render(request, 'blog/post_edit.html', context)
    else:
        messages.info(request, 'У вас недостаточно прав для создания записи')
        return redirect('post_list')


def post_edit(request, pk):
    """Редактирование существующей записи"""
    if not request.user.is_authenticated:  # Проверка авторизации
        messages.info(request, 'Вы не авторизованны! Войдите в аккаунт')
        return redirect('sing_in')
    author_name = Post.objects.get(pk=pk).author  # Из базы данных получаем вызываемую запись и выбираем автора
    if edit_post(request) != 1:
        if request.user.username != author_name.username:  # Если человек не является автором - редакция запрещена
            messages.info(request, 'Это не ваша запись и вы не можете её редактировать')
            return redirect('post_list')
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":  # Если пользователь отправляет данные
        form = PostForm(request.POST, instance=post)  # В Post - форму становится возможным внести изменения и сохранить
        if form.is_valid():
            post = form.save(commit=False)  # commit равный False указывает на то, что форма готова к сохранению,
            # но в нее нужно еще внести изменения и сохранение произойдет после повторного вызова метода save()
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            messages.success(request, 'Пост успешно изменен')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'blog/post_edit.html', context)


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
    context = {
        'posts': posts,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
        'count_posts': count_posts
    }
    return render(request, 'blog/by_rubric.html', context)


def delete_post(request, pk):
    if not request.user.is_authenticated:  # Проверка авторизации
        messages.info(request, 'Вы не авторизованны! Войдите в аккаунт')
        return redirect('sing_in')
    author_name = Post.objects.get(pk=pk).author  # Из базы данных получаем вызываемую запись и выбираем автора
    if edit_post(request) != 1:
        if request.user.username != author_name.username:  # Если человек не является автором - удаление запрещено
            messages.info(request, 'Это не ваша запись и вы не можете её удалить')
            return redirect('post_list')
    # if request.method == "POST":
    post = Post.objects.get(pk=pk)
    post.delete()
    messages.success(request, 'Пост успешно удалён')
    return redirect('post_list')


def home(request):
    return redirect('post_list')


def add_rating(request, pk):
    # print(request.user.id)
    # print(pk)
    # print(request.POST.get('rating'))
    this_post = Post.objects.get(pk=pk).title
    if request.method == 'POST':
        if request.user.is_anonymous:
            messages.info(request, 'Авторизуйтесь, что бы оценить пост')
        else:
            # Need ValueRatingPost.objects.update_or_create()
            # ValueRatingPost.objects.update_or_create(defaults={'rating_id': 4},
            # user=User.objects.get(username='admin'),  post=Post.objects.get(id=1))

            form = RatingForm(request.POST)
            if form.is_valid():
                ValueRatingPost.objects.update_or_create(defaults={'rating_id': int(request.POST.get('rating'))},
                                                         user_id=request.user.id,
                                                         post_id=pk)

                # rating = form.save(commit=False)
                # rating.user = request.user
                # rating.save()
                return redirect('post_detail', pk=pk)

    context = {
        'this_post': this_post,
    }
    return render(request, 'blog/add_rating.html', context)
