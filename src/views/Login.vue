<template>
  <form class=""></form>
</template>

<script>
import messages from "@/utils/messages";

export default {
  name: "Login",
  mounted() {
    if (messages[this.$route.query.message]) {
      this.$message(messages[this.$route.query.message])
    }
  },
}

</script>
