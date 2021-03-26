<template>
<Header/>
<div class="container content">
  <Tags/>
  <div class="container container--content">
    <NewPost_link/>
    <router-view/>
    <ModalWindow />
  </div>
</div>
</template>

<script>
import Header from "@/components/Header";
import Tags from "@/components/Tags";
import NewPost_link from "@/components/NewPost_link";
import ModalWindow from "@/components/ModalWindow";

export default {
  name: "MainLayout",
  data() {
    return {
    }
  },
  components: {
    Tags,
    Header,
    NewPost_link,
    ModalWindow
  },

}

</script>

<style scoped>

</style>