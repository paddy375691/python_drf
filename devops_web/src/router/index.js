import { createRouter, createWebHistory } from 'vue-router'
import Layout from '../views/Layout.vue'

const routes = [
  {
    path: '/',
    name: "首页",
    component: Layout,
    redirect: '/dashboard',
    children: [
      {
        path: '/dashboard',
        name: "仪表盘",
        icon: "HomeFilled",
        component: () => import('../views/Dashboard')
      },
    ]
  },
  {
    path: "/host",
    name: "主机管理",
    icon: "Platform",
    component: Layout,
    children: [
      {
        path: "/host/idc",
        name: "机房管理",
        component: ()=>import('../views/idc/Idc')
      },
      {
        path: "/host/server_group",
        name: "主机分组",
        component: ()=>import('../views/servergroup/ServerGroup')
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
