import { createRouter, createWebHashHistory } from 'vue-router';

const routes = [
    {
        path: '/',
        name: 'Home',
        meta: { layout: 'main'},
        component: () => import("@/views/Home.vue"),
    },

    {
        path: '/post_set/:id',
        name: 'Post',
        meta: { layout: 'main'},
        component: () => import("@/views/Post.vue"),
        props: true
    },

    {
        path: '/tags_list/:id',
        name: 'Tag',
        meta: { layout: 'main'},
        component: () => import("@/views/Tag.vue"),
        props: true
    },

    {
        path: '/login',
        name: 'Login',
        meta: { layout: 'empty'},
        component: () => import("@/views/Login.vue"),
    },

    {
    path: "/registration",
    name: "Registration",
    meta: { layout: "empty" },
    component: () => import("@/views/Registration.vue"),
    },


]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
