// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// npm run dev
import Vue from 'vue'
import Vuex from 'vuex';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App'
import router from './router'
import http from './http'
import util from './utils/util'
import store from './assets/store'

// prototype
Vue.prototype.axios = http.axios;
Vue.prototype.log = util.log;

Vue.config.productionTip = false
Vue.use(ElementUI, { size: 'normal' });

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
  // components: { App },
  // template: '<App/>',
})
