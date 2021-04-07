<template>
  <div class="container_nav">
    <div class="container__tags">
      <p class="tags__title">Навигация по тегам:</p>
      <ul>
        <li
          class="tags__text"
          v-for="tag in Tags"
          :key="tag.id"
        >
          <router-link
            class="nav__link"
            :to="{name: 'Tag', path: `tags_list/${tag.id}`, params: {id: tag.id}}"
          >
            {{ tag.rubric }}
          </router-link>
        </li>
      </ul>
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
      load: null
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
    },
  },
}
</script>