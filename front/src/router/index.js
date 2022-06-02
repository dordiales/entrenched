import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  {
    path: '/game/:gameId',
    name: 'Game',
    component: () => import('@/pages/game/GamePage.vue'),
  },
  {
    path: '/game/:gameId/:playerId',
    name: 'Player',
    component: () => import('@/pages/player/PlayerPage.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
