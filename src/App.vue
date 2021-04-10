<template>
  <div class="app">
    <component :is="layout">
      <router-view />
    </component>
  </div>
</template>

<script>
import MainLayout from "@/layout/MainLayout";
import EmptyLayout from "@/layout/EmptyLayout";
import VoidLayout from "@/layout/VoidLayout";

export default {
  name: "App",
  components: {
    MainLayout,
    EmptyLayout,
    VoidLayout,
  },

  computed: {
    layout() {
      return (this.$route.meta.layout || "empty") + "-layout";
    },
  },
};
</script>

<style>
@import "assets/style.css";
@import "~materialize-css/dist/css/materialize.min.css";
</style>
