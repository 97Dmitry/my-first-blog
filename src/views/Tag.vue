<template>
  <h1>Some tag and posts</h1>
</template>

<script>
export default {
  name: "Tag",
  props: ['id'],

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

  }
}
</script>

<style scoped>

</style>