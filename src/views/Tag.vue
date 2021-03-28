<template>
<div>
  <p>Всего записей: {{ Posts.length }}</p>
  <div v-for="post in Posts" :key="post.id" class="post">
    <main>
      <h4 class="post__title post__title__link" href="#" @click="goToPost(post.id)">{{ post.title }}</h4>
      <div class="user">
        <img class="user_pic" style="width: 74px; height: 74px;"
             :src="Profile[checkIndex(Profile, post)].picture" alt="">
        <div class="user_info">
          <div class="user_name">{{ (post.author) }}</div>
          <div>
            {{ Profile[checkIndex(Profile, post)].user_rank }}
          </div>
        </div>
      </div>
      <p>Тег: <a class="tags__text" href="">{{ post.rubric }}</a></p>
      <div class="date">
        <p class="post__published_date">Дата публикации: {{ $parseDate(post.created_date) }}</p>
      </div>
      <details>
        <summary>Развернуть</summary>
        <p v-html="post.text"></p>
      </details>
      <hr style="color: white; border: 1px solid"/>
    </main>
  </div>
  <hr/>
</div>
</template>

<script>

export default {
  name: "Tag",
  props: ['id'],

  components: {},

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