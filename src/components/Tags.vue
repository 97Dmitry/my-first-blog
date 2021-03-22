<template>
  <div class="container_nav">
    <div class="container__tags">
      <p class="tags__title">Навигация по тегам</p>
      <div v-for="tag in Tags" :key="tag.id">
        <ul>
          <li class="tags__text" href="#" @click="goToTag(tag.id)">{{ tag.rubric }}</li>
        </ul>
      </div>
    </div>
    <div class="container__chat_link">
      <a class="chat__link" href="">Ссылка на чат</a>
    </div>
  </div>
</template>

<script>

export default {
  name: "Tags",

  data() {
    return {
      Tags: [],

    }
  },

  created() {
    this.loadTags();
  },

  methods: {
    async loadTags() {
      this.Tags = await fetch(
          `${this.$store.getters.getServerUrl}/tags_list`
      ).then(response => response.json())
      console.log(this.Tags)
    },

    goToTag(id) {
      this.$router.push({name: 'Tag', params: {id: id}})
    },
  },

}
</script>

<style scoped>

.container--content {
  margin-left: 5px;
}

</style>