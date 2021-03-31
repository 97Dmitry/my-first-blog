import { createStore } from 'vuex'
import auth from "./auth"

const store = createStore({
  state: {
    backendUrl: 'http://127.0.0.1:8000/api'
  },
  mutations: {

  },
  actions: {

  },
  modules: {
    auth
  },
  getters: {
    getServerUrl: state => {
      return state.backendUrl
    }
  },
})

export default store
