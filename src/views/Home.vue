<template>
  <div class="container_nav">
    <div class="container__tags">
      <p class="tags__title">Навигация по тегам</p>
      <div v-for="tag in Tags" :key="tag.id">
        <ul>
          <li><a class="tags__text" href="">{{ tag.rubric }}</a></li>
        </ul>
      </div>
    </div>
    <div class="container__chat_link">
      <a class="chat__link" href="">Ссылка на чат</a>
    </div>
  </div>
  <div class="container container--content">
    <NewPost_link/>
    <p>Всего записей: {{ Posts.length }}</p>
    <div v-for="post in Posts" :key="post.id" class="post">
      <main>
        <h2 class="post__title post__title__link" href="#" @click="goTo(post.id)">{{ post.title }}</h2>
        <div class="media text-muted pt-3">
          <img class="mr-2 rounded" style="width: 58px; height: 58px;"
               :src="Profile[checkIndex(Profile, post)].picture" alt="">
          <div class="mb-1">
            <p><strong class="d-block">{{ post.author }}</strong>
              <span v-for="rank in Profile[checkIndex(Profile, post)].user_rank" :key="rank.id">
                  <span> {{ rank }}, </span>
                </span>
            </p>
          </div>
        </div>
        <p>Тег: <a class="tags__text" href="">{{ post.rubric }}</a></p>
        <div class="date">
          <p class="post__published_date">Дата публикации: {{ post.created_date }}</p>
        </div>
        <details>
          <summary>Развернуть</summary>
          <p v-html="post.text"></p>
        </details>
        <hr/>
      </main>
    </div>
    <nav aria-label="...">
      <ul class="pagination">
        <li class="page-item {% if not prev_url %} disabled {% endif %}">
          <a class="page-link" href="">Предыдущая страница</a>
        </li>
        <li class="page-item active" aria-current="page">
          <a class="page-link" href=""></a>
        </li>
        <li class="page-item">
          <a class="page-link" href=""></a>
        </li>
        <li class="page-item {% if not next_url %} disabled {% endif %}">
          <a class="page-link" href="">Следующая страница</a>
        </li>
      </ul>
    </nav>
    <hr/>
  </div>
</template>


<script>
import NewPost_link from "@/components/NewPost_link";

export default {
  name: 'Home',
  title: "BlogPost",

  data() {
    return {
      Posts: [],
      Tags: [],
      Profile: [],

    }
  },
  components: {
    NewPost_link,

  },
  created() {
    this.loadListPosts();
    this.loadTagsPosts();
    this.loadProfilePosts();


  },
  methods: {
    async loadListPosts() {
      this.Posts = await fetch(
          `${this.$store.getters.getServerUrl}/post_list`
      ).then(response => response.json())
      console.log(this.Posts)
    },

    async loadTagsPosts() {
      this.Tags = await fetch(
          `${this.$store.getters.getServerUrl}/tags_list`
      ).then(response => response.json())
      console.log(this.Tags)
    },

    async loadProfilePosts() {
      this.Profile = await fetch(
          `${this.$store.getters.getServerUrl}/profile_list`
      ).then(response => response.json())
      // console.log(this.Profile)
    },

    checkIndex(profile, post) {
      let a = 0
      profile.findIndex(function (element, index) {
        if (element.user === post.author) {
          return a = index
        }
      })
      return a
    },

    goTo(id) {
      this.$router.push({name: 'Post', params: {id: id}})
    }


  }

}
</script>

<style scoped>

.container--content {
  margin-left: 5px;
}


</style>