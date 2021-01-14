<template>
  <div class="app">
    <Header />
    <div class="container content">
      <router-view/>
    </div>
  </div>
</template>

<script>

import Header from "@/components/Header";

export default {
  name: 'App',
  components: {
    Header,

  }
}
</script>


<style>
@import "../static/css/style.css";
</style>

