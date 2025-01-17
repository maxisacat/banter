import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../views/Login.vue")
    },
    {
      path: "/signup",
      name: "signup",
      component: () => import("../views/Signup.vue")
    },
    {
      path: "/profile",
      name: "profile",
      component: () => import("../views/Profile.vue")
    },
    {
      path: "/profile/:id",
      name: "profileId",
      component: () => import("../views/Profile.vue")
    },
    {
      path: "/room/:id",
      name: "room",
      component: () => import("../views/Room.vue")
    },
    {
      path: "/invites",
      name: "invites",
      component: () => import("../views/Invites.vue")
    }
  ]
})

export default router
