import store from "@/store/index";

export default {
  actions: {
    async accountRegistration({dispatch}, {username, email, password}) {
      const server = store.getters.getServerUrl
      await fetch(`${server}/auth/users/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            "email": email,
            "username": username,
            "password": password
          })
        }
      ).then(response => {
        response.json()
      })
    }
  }
}