<template>
  <div class="container container--content">
    <NewPost_link/>
    <h2 class="post__title">{{ Post.title }}</h2>
    <div class="date">
      <p class="post__published_date">Дата публикации: {{ Post.created_date }}</p>
    </div>
            <p> Рейтинг записи: {{ Rating.avg }} из {{ Rating.length }} проголосовавших </p>
    <div class="media text-muted pt-3">
      <img class="mr-2 rounded" style="width: 58px; height: 58px;" :src="Profile[checkIndex(Profile, Post.author)].picture" alt="">
      <p class="mb-1 ml-1 middle lh-sm"><strong class="d-block">@{{ Post.author }}</strong>Автор записи</p>
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
            <p> Дата написания: {{ comment.created }} </p>
          </div>
          <p> Комментарий: </p>
          <p class="ml-2"> {{ comment.comment }} </p>
          <hr/>
          <!--                            {% endfor %}-->
        </div>
      </details>
      <hr/>
      <h5>Создать свой комментарий:</h5>
      <!--            <details>-->
      <!--                <form method="POST" class="post-form">-->
      <!--                    {% csrf_token %}-->
      <!--                    <p> Комментарий: <br/>{{ form.comment }} <br/> {{ form.comment.help_text }} </p>-->
      <!--                    <p> Email: <br/>{{ form.email }} </p>-->
      <!--                    <button type="submit" class="save btn btn-success">Создать</button>-->
      <!--                    {{ form.captcha }}-->
      <!--                </form>-->
      <!--            </details>-->
      <hr/>
    </div>
    <a href="">Оценить пост</a>
    <hr/>
    <p>Для редактирования записи нажмите сюда - <a href="#">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-pencil-fill" fill="currentColor"
           xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd"
              d="M12.854.146a.5.5 0 0 0-.707 0L10.5 1.793 14.207 5.5l1.647-1.646a.5.5 0 0 0 0-.708l-3-3zm.646 6.061L
                      9.793 2.5 3.293 9H3.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.
                      5v.207l6.5-6.5zm-7.468 7.468A.5.5 0 0 1 6 13.5V13h-.5a.5.5 0 0 1-.5-.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a
                      .5.5 0 0 1-.5-.5V10h-.5a.499.499 0 0 1-.175-.032l-.179.178a.5.5 0 0 0-.11.168l-2 5a.5.5 0 0 0 .65.65l5
                      -2a.5.5 0 0 0 .168-.11l.178-.178z"/>
      </svg>
    </a></p>
    <p>Для удаления записи нажмите сюда - <a id="deleter" href="#">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-trash-fill" fill="currentColor"
           xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd"
              d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0
                       0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5z
                       M8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5a.5.5 0 0 0-1 0v7a.5.5 0 0 0 1 0v-7z"/>
      </svg>
    </a></p>
  </div>
</template>

<script>
import NewPost_link from "@/components/NewPost_link";

export default {
  name: "Post",
  props: ['id'],
  title: 'this.Post.title',

  data() {
    return {
      Post: [],
      Tag: [],
      Profile: [],
      Rating: [],
      Comments: []

    }
  },

  components: {
    NewPost_link,


  },
  created() {
    this.loadPost();
    this.loadCommentsPosts();
    this.loadProfilePosts();
    this.loadRatingPosts()
    // console.log(`${this.Post}`)
  },

  methods: {
    async loadPost() {
      this.Post = await fetch(
          `${this.$store.getters.getServerUrl}/post/${this.id}`
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
      Object.assign(this.Rating, { avg: (this.Rating.reduce((total, rating) => total + rating.rating, 0) / this.Rating.length)});
      // console.log(this.Rating)
    },
    async loadCommentsPosts() {
      this.Comments = await fetch(
          `${this.$store.getters.getServerUrl}/comment_list/${this.id}`
      ).then(response => response.json())
    },

    // AvgRating() {
    //   this.Rating.avg = (this.Rating.reduce((total, rating) => {total + rating.rating}, 0) / this.Rating.length)
    //   console.log(this.Rating.avg, this.Rating)
    // }
  },

}

</script>

<style scoped>
.container--content {
  margin: 0 auto;
}
</style>