<template>
  <h4 class="post__title">{{ Post.title }}</h4>
  <div class="date">
    <p class="post__published_date">Дата публикации: {{ $parseDate(Post.created_date) }}</p>
  </div>
  <p> Рейтинг записи: {{ Rating.avg }} из {{ Rating.length }} проголосовавших </p>
  <div class="user">
    <img class="user_pic" style="width: 74px; height: 74px;"
         :src="Profile[checkIndex(Profile, post)].picture" alt="">
    <div class="user_info">
      <div class="user_name">{{ Post.author }}</div>
      <div>
        {{ Profile[checkIndex(Profile, Post)].user_rank }}
      </div>
    </div>
  </div>
  <p>Тег: <a class="tags__text" href="#">{{ Post.rubric }}</a></p>
  <div class="text">
    <hr/>
    <p class="text" v-html="Post.text"></p>
    <hr/>
    <h5>Комментарии:</h5>
    <details>
      <div v-for="comment in Comments" :key="comment.id" class="comments">
        <!--                            {% for comment in comments %}-->
        <div class="media text-muted pt-3">
          <img class="mr-2 rounded" style="width: 58px; height: 58px;"
               :src="Profile[checkIndex(Profile, comment.name)].picture" alt="">
          <p class="mb-1 ml-1 small lh-sm"><strong class="d-block">{{ comment.name }}</strong>Автор
            комментария</p>
        </div>
        <div class="date">
          <p> Дата написания: {{ $parseDate(comment.created) }} </p>
        </div>
        <p> Комментарий: </p>
        <p class="ml-2"> {{ comment.comment }} </p>
        <hr/>
        <!--                            {% endfor %}-->
      </div>
    </details>
    <hr/>
    <h5>Создать свой комментарий:</h5>
    <!--                  <details>-->
    <!--                      <form method="POST" class="post-form">-->
    <!--                          <p> Комментарий: <br/>{{ form.comment }} <br/> {{ form.comment.help_text }} </p>-->
    <!--                          <p> Email: <br/>{{ form.email }} </p>-->
    <!--                          <button type="submit" class="save btn btn-success">Создать</button>-->
    <!--                          {{ form.captcha }}-->
    <!--                      </form>-->
    <!--                  </details>-->
    <hr/>
  </div>
  <a href="">Оценить пост</a>
  <hr/>
  <p>Для редактирования записи нажмите сюда - <a href="#">
    <i class="material-icons">build</i>
  </a></p>
  <p>Для удаления записи нажмите сюда - <a id="deleter" href="#">
    <i class="material-icons">delete</i>
  </a></p>
</template>

<script>


export default {
  name: "Post",
  props: ["id"],
  data() {
    return {
      Post: [],
      Tag: [],
      Profile: [],
      Rating: [],
      Comments: []


    }
  },
  components: {},
  created() {
    this.loadPost();
    this.loadCommentsPosts();
    this.loadProfilePosts();
    this.loadRatingPosts()
  },
  methods: {
    async loadPost() {
      this.Post = await fetch(
        `${this.$store.getters.getServerUrl}/posts_list/${this.id}`
      ).then(response => response.json())
      // console.log(this.Post, this.id)

    },

    async loadTagsPosts() {
      this.Tag = await fetch(
        `${this.$store.getters.getServerUrl}/tags_list`
      ).then(response => response.json())
      // console.log(this.Tags)
    },

    async loadProfilePosts() {
      this.Profile = await fetch(
        `${this.$store.getters.getServerUrl}/profile_list`
      ).then(response => response.json())
      // console.log(this.Profile)
    },

    checkIndex(profile, name) {
      let a = 0
      profile.findIndex(function (element, index) {
        if (element.user === name) {
          return a = index
        }
      })
      return a
    },

    async loadRatingPosts() {
      this.Rating = await fetch(
        `${this.$store.getters.getServerUrl}/cur_rating/${this.id}`
      ).then(response => response.json());
      Object.assign(this.Rating, {avg: (this.Rating.reduce((total, rating) => total + rating.rating, 0) / this.Rating.length)});
    },

    async loadCommentsPosts() {
      this.Comments = await fetch(
        `${this.$store.getters.getServerUrl}/comments_list/${this.id}`
      ).then(response => response.json())
    }
  },
}
</script>
