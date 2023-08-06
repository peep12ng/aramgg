import { createWebHistory, createRouter } from "vue-router";
import Home from "./components/Home.vue"
import Summoner from "./components/Summoner.vue"
import Hello from "./components/Hello.vue"

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/summoner/:id',
    component: Summoner
  },
  {
    path: '/Hello',
    component: Hello
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior (to, from, savedPosition){ // eslint-disable-line no-unused-vars
    return { top: 0 }
  }
});

export default router; 