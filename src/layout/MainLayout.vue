<template>
  <div>
    <Header />
    <div class="container_style content">
      <Tags v-on:sendRequest="requestReload" />
      <div class="container--content">
        <NewPost_link />
        <router-view :key="$route.fullPath" />
        <!--    <ModalWindow />-->
      </div>
    </div>
  </div>
</template>

<script>
import Header from "@/components/Header";
import Tags from "@/components/Tags";
import NewPost_link from "@/components/NewPost_link";
// import ModalWindow from "@/components/ModalWindow";

export default {
  name: "MainLayout",
  components: {
    Tags,
    Header,
    NewPost_link,
    // ModalWindow
  },
  data() {
    return {};
  },
  methods: {},
};
</script>
