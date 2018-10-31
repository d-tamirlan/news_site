import Vue from 'vue'
import Router from 'vue-router'
import App from './App.vue'
import News from './Components/News.vue'

Vue.use(Router);

const router = new Router({
 routes: [
   // {
   //   path: '/',
   //   name:'newsList',
   //   component: App
   // },
   {
     path: '/news/:id',
     name:'news',
     component: News,
     props: true,
   },
 ]
})

new Vue({
  el: '#app',
  render: h => h(App),
  router
})
