import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import store from "@/store";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/profile',
        name: 'profile',
        meta: {
            requiresAuth: true
        },
        component: () => import(/* webpackChunkName: "about" */ '../views/ProfileView.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (store.getters["auth/isLoggedIn"]) {
            next()
            return
        }
        next('/login')
    } else {
        next()
    }
})

export default router
