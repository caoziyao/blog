import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/pages/index'
import Blog from '@/pages/blog'
import Edit from '@/pages/edit'
import Book from '@/pages/book'
import Todo from '@/pages/todo'
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
    },
    {
      path: '/book',
      name: 'book',
      component: Book
    },
    {
      path: '/todo',
      name: 'todo',
      component: Todo
    }
  ]
})
