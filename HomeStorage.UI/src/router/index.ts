import { createRouter, createWebHistory } from 'vue-router'

const DashBoard = () => import('../pages/DashBoard.vue')
const FileManager = () => import('../pages/FileManager.vue')

const app_routes = [
  { path: '/', redirect: '/dashboard' },
  { path: '/dashboard', name: 'dashboard', component: DashBoard, meta: { title: 'HomeStorage | Dashboard' } },
  { path: '/files', name: 'files', component: FileManager, meta: { title: 'HomeStorage | Files' } },
  { path: '/:pathMatch(.*)*', redirect: '/' },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: app_routes,
})

export default router
