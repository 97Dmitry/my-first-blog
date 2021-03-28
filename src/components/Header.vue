<template>
<header class="header">
  <div class="container_style">

    <div class="header__inner">

      <a class="header__logo" href="" @click="goTo()">BlogPost</a>

      <div class="nav">
        <router-link class="nav__link" to="/login">Авторизоваться</router-link>
        <router-link class="nav__link" to="/registration">Зарегистрироваться</router-link>
        <a class="nav__link" href="">Моя страница <br> #User# </a>
        <a class="nav__link nav__link--red" href="" v-on:click.prevent="logout()">Выйти</a>
      </div>

    </div>
  </div>
</header>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {}
  },

  methods: {
    logout() {
      this.$router.push({path: "/login", query: {message: "logout"}});
    },
    goTo() {
      this.$router.push({name: `Home`})
    },
  }
}
</script>

<style scoped>

</style>