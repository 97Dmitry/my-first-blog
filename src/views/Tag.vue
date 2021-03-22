<template>
  <Tags/>
  <div class="container container--content">
    <NewPost_link/>
    <p>Всего записей: {{ Posts.length }}</p>
    <div v-for="post in Posts" :key="post.id" class="post">
      <main>
        <h2 class="post__title post__title__link" href="#" @click="goToPost(post.id)">{{ post.title }}</h2>
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
import Tags from "@/components/Tags";
import NewPost_link from "@/components/NewPost_link";


export default {
  name: "Tag",
  props: ['id'],

  components: {
    Tags,
    NewPost_link
  },

  data() {
    return {
      Posts: [],
      Tag: [],
      Profile: [],
      }
  },

  created() {
    this.loadPosts();
    this.loadTag();
    this.loadProfilePosts();


  },

  methods: {
    async loadPosts() {
      this.Posts = await fetch(
          `${this.$store.getters.getServerUrl}/tag_posts/${this.id}`
      ).then(response => response.json())
      console.log(this.Posts)
    },

    async loadTag() {
      this.Tag = await fetch(
          `${this.$store.getters.getServerUrl}/cur_tag/${this.id}`
      ).then(response => response.json())
      console.log(this.Tag)
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

    goToPost(id) {
      this.$router.push({name: 'Post', params: {id: id}})
    },

  }
}
</script>

<style scoped>

</style>