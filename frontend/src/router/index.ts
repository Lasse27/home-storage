import { createRouter, createWebHistory } from 'vue-router'
import { nextTick } from 'vue';

const DashBoard = () => import('@/pages/DashBoard.vue')
const FileManager = () => import('@/pages/FileManager.vue')
const Settings = () => import('@/pages/Settings.vue')
const System = () => import('@/pages/SystemOverview.vue')
const app_routes = [
  { path: '/', redirect: '/dashboard' },
  { path: '/dashboard', name: 'dashboard', component: DashBoard, meta: { title: 'HomeStorage | Dashboard' } },
  { path: '/files', name: 'files', component: FileManager, meta: { title: 'HomeStorage | Files' } },
  { path: '/system', name: 'system', component: System, meta: { title: 'HomeStorage | System' } },
  { path: '/settings', name: 'settings', component: Settings, meta: { title: 'HomeStorage | Settings' } },
  { path: '/:pathMatch(.*)*', redirect: '/' },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: app_routes,
})

const DEFAULT_TITLE = 'HomeStorage';
router.afterEach((to, from) => {
  // Use next tick to handle router history correctly
  // see: https://github.com/vuejs/vue-router/issues/914#issuecomment-384477609
  nextTick(() => {
    document.title = (to.meta.title as string) || DEFAULT_TITLE;
  });
});

export default router
