import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router"
//import HomeView from "./pages/HomeView.vue"
import { libName } from "./conf"
// @ts-ignore
import { default as autoRoutes } from '~pages'

const baseTitle = libName;

const routes: Array<RouteRecordRaw> = [
  /*{
    path: "/",
    component: HomeView,
    meta: {
      title: "Home"
    }
  },*/
  ...autoRoutes,
  /*{
    path: "/path+",
    component: () => import("./views/PageView.vue"),
  }*/
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

router.afterEach((to, from) => {
  window.scrollTo(0, 0);
  if ("id" in to.params) {
    let buf = new Array<string>();
    if ("category" in to.params) {
      buf.push(to.params.category.toString());
    }
    if ("id" in to.params) {
      buf.push(to.params.id.toString());
    }
    document.title = `${baseTitle} - ${buf.join("/")}`
  }
  else if (to.meta?.title) {
    document.title = `${baseTitle} - ${to.meta?.title}`
  }
});

export default router