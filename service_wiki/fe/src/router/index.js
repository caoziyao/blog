import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/pages/index'
import Blog from '@/pages/blog'
import Edit from '@/pages/edit'
import Book from '@/pages/book'
import Todo from '@/pages/todo'
import Video from '@/pages/video'
import Login from '@/pages/login'
import FeedBack from '@/pages/feedback'
import MzNv from '@/pages/mznv'
import Music from '@/pages/music'

Vue.use(Router)

export default new Router({
  linkActiveClass: 'link-active',
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
    },
    {
      path: '/video',
      name: 'video',
      component: Video
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/feedback',
      name: 'feedback',
      component: FeedBack
    },
    {
      path: '/mznv',
      name: 'mznv',
      component: MzNv,
    },
    {
      path: '/music',
      name: 'music',
      component: Music,
    },
  ]
})
