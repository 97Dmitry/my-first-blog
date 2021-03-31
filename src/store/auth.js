export default {
  actions: {
    async accountRegistration({dispatch}, {username, email, password}) {
      const server = "http://127.0.0.1:8000/api"
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