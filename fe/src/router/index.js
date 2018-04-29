import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/pages/index'
import Blog from '@/pages/blog'
import Edit from '@/pages/edit'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/blog',
      name: 'blog',
      component: Blog
    },
    {
      path: '/edit',
      name: 'edit',
      component: Edit
    }
  ]
})
