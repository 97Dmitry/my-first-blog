import {createRouter, createWebHistory} from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'Home',
    meta: {layout: 'main'},
    component: () => import("@/views/Home.vue"),
  },

  {
    path: '/post_set/:id',
    name: 'Post',
    meta: {layout: 'main'},
    component: () => import("@/views/Post.vue"),
    props: true
  },

  {
    path: '/tags_list/:id',
    name: 'Tag',
    meta: {layout: 'main'},
    component: () => import("@/views/Tag.vue"),
    props: true
  },

  {
    path: '/login',
    name: 'Login',
    meta: {layout: 'empty'},
    component: () => import("@/views/Login.vue"),
  },

  {
    path: "/registration",
    name: "Registration",
    meta: {layout: "empty"},
    component: () => import("@/views/Registration.vue"),
  },

  {
    path: "/not_found",
    name: "NotFoundComponent",
    meta: {layout: "void"},
    component: () => import("@/views/NotFoundPage.vue")
  },

  {
    path: '/:pathMatch(.*)*',
    redirect: { name: 'NotFoundComponent' }
  }


]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
