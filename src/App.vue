<template>
  <div id="app">
    <component :is="layout">
      <router-view />
    </component>
  </div>
</template>

<script>
import MainLayout from "@/layout/MainLayout";
import EmptyLayout from "@/layout/EmptyLayout";

export default {
  name: 'App',
  components: {
    MainLayout,
    EmptyLayout
  },

  computed: {
    layout() {
      return (this.$route.meta.layout  || "empty") + "-layout";
    }
  }

}
</script>


<style>
@import "assets/style.css";
</style>

