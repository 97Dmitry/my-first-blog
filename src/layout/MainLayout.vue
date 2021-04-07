<template>
<Header/>
<div class="container_style content" v-if="isOpen">
  <Tags/>
  <div class="container--content">
    <NewPost_link/>
    <router-view/>
<!--    <ModalWindow />-->
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
  data() {
    return {
      isOpen: 1
    }
  },
  components: {
    Tags,
    Header,
    NewPost_link,
    // ModalWindow
  },

}

</script>