<template>
  <header class="header">
    <div class="container">

      <div class="header__inner">

        <a class="header__logo" href="#">BlogPost</a>

        <nav class="nav">
          <!--                    {% if user.is_anonymous %}-->
          <a class="nav__link" href="#">Авторизоваться</a>
          <a class="nav__link" href="#">Зарегистрироватья</a>
          <!--                    {% endif %}-->
          <!--                    {% if user.is_authenticated %}-->
          <a class="nav__link" href="#">Моя страница <br> #USER# </a>
          <a class="nav__link nav__link--red" href="#">Выйти</a>
          <!--                    {% endif %}-->
        </nav>

      </div>
    </div>
  </header>

  <div class="container content">
    <!--        {% block left_nav %}-->
    <div class="container_nav">
      <div class="container__tags">
        <p class="tags__title">Навигация по тегам</p>
        <!--        {% for tag in tags %}-->
<!--        <div v-for="tag in Posts.tags" :key="tag.id"></div>-->
          <ul>
            <li><a class="tags__text" href="#">tag</a></li>
          </ul>
        <!--        {% endfor %}-->
      </div>
      <div class="container__chat_link">
        <a class="chat__link" href="#">Сслыка на чат</a>
      </div>
    </div>
    <!--        {% endblock %}-->
    <div class="container container--content">
      <p class="new_post">
        <a href="#">
          <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-file-text" fill="currentColor"
               xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
                  d="M4 0h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2zm0 1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H4z"/>
            <path fill-rule="evenodd"
                  d="M4.5 10.5A.5.5 0 0 1 5 10h3a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5zm0-2A.5.5 0 0 1 5 8h6a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5zm0-2A.5.5 0 0 1 5 6h6a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5zm0-2A.5.5 0 0 1 5 4h6a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/>
          </svg>
        </a> <span> &lt;- для создания нового поста, нажмите сюда </span>
      </p>
      <!--      {% block content %}-->
      <p>Всего записей: </p>
      <div v-for="post in Posts" :key="post.id" class="post">
        <main>
<!--          {% for post in page %}-->
          <h2 class="post__title"><a class="post__title__link" href="#">{{post.title}}</a></h2>
          <div class="media text-muted pt-3">
            <img class="mr-2 rounded" style="width: 38px; height: 38px;" src="#post.author.profile.picture.url#"
                 alt="">
            <p class="mb-1 ml-1 small lh-sm"><strong class="d-block">{{post.author}}</strong>
<!--              {% for i in post.author.profile.user_rank.all %}-->
<!--              {{ i }},-->
<!--              {% endfor %}-->
            </p>
          </div>
          <p>Тег: <a class="tags__text" href="#">{{post.rubric}}</a></p>
          <div class="date">
            <p class="post__published_date">Дата публикации: {{post.created_date}}</p>
          </div>
          <details>
            <summary>Развернуть</summary>
            <p>{{post.text}}</p>
          </details>
          <hr/>
<!--          {% endfor %}-->
        </main>
        <nav aria-label="...">
          <ul class="pagination">
            <li class="page-item {% if not prev_url %} disabled {% endif %}">
              <a class="page-link" href="#">Предыдущая страница</a>
            </li>
<!--            {% for n in page.paginator.page_range %}-->
<!--            {% if page.number == n %}-->
            <li class="page-item active" aria-current="page">
              <a class="page-link" href="#"></a>
            </li>
<!--            {% elif n > page.number|add:-3 and n < page.number|add:3 %}-->
            <li class="page-item">
              <a class="page-link" href="#"></a>
            </li>
<!--            {% endif %}-->
<!--            {% endfor %}-->
            <li class="page-item {% if not next_url %} disabled {% endif %}">
              <a class="page-link" href="#">Следующая страница</a>
            </li>
          </ul>
        </nav>
        <hr/>
      </div>
      <!--      {% endblock %}-->
      <div class="link">
        <p>Для подробной информации, обращайтесь по адресу: <a href="#">link</a></p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      Posts: [],
      Tags: [],

    }
  },
  components: {},
  created() {
    this.loadListPosts()

  },
  methods: {
    async loadListPosts() {
      this.Posts = await fetch(
          `${this.$store.getters.getServerUrl}/post_list`
      ).then(response => response.json())
      // console.log(this.Posts)
    }
  }
}
</script>

<style>


</style>