<template>
<header class="header">
  <div class="container">

    <div class="header__inner">

      <a class="header__logo" href="">BlogPost</a>

      <div class="nav">
        <router-link class="nav__link" to="/login">Авторизоваться</router-link>
        <router-link class="nav__link" to="/registration">Зарегистрироваться</router-link>
        <a class="nav__link" href="">Моя страница <br> #User# </a>
        <a class="nav__link nav__link--red" href="">Выйти</a>
      </div>

    </div>
  </div>
</header>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style scoped>

</style>