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
      <div class="home_page__text" id="post_text" :class="{ full: isOpen }">
        <!--          <details>-->
        <!--            <summary>Развернуть</summary>-->
        <p v-html="post.text"></p>
        <div class="bottom" :class="{ full2: isOpen }"></div>
        <!--          </details>-->
      </div>
      <a href="" v-on:click.prevent="isOpen = !isOpen">Читать дальше</a>
      <hr style="color: white; border: 1px solid"/>
    </main>
  </div>
  <!--  <div aria-label="...">-->
  <!--    <ul class="pagination">-->
  <!--      <li class="page-item {% if not prev_url %} disabled {% endif %}">-->
  <!--        <a class="page-link" href="">Предыдущая страница</a>-->
  <!--      </li>-->
  <!--      <li class="page-item active" aria-current="page">-->
  <!--        <a class="page-link" href=""></a>-->
  <!--      </li>-->
  <!--      <li class="page-item">-->
  <!--        <a class="page-link" href=""></a>-->
  <!--      </li>-->
  <!--      <li class="page-item {% if not next_url %} disabled {% endif %}">-->
  <!--        <a class="page-link" href="">Следующая страница</a>-->
  <!--      </li>-->
  <!--    </ul>-->
  <!--  </div>-->
  <hr/>
</div>
</template>


<script>

export default {
  name: 'Home',
  title: "BlogPost",

  data() {
    return {
      Posts: [],
      Profile: [],
      isOpen: false

    }
  },
  components: {},
  created() {
    this.loadListPosts();
    this.loadProfilePosts();
  },
  methods: {
    async loadListPosts() {
      this.Posts = await fetch(
        `${this.$store.getters.getServerUrl}/posts_list`
      ).then(response => response.json())
    },
    async loadProfilePosts() {
      this.Profile = await fetch(
        `${this.$store.getters.getServerUrl}/profile_list`
      ).then(response => response.json())
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
    }
  }
}
</script>

<style scoped>

</style>