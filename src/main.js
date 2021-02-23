import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import axios from 'axios'
import vuetify from './plugins/vuetify';
import router from './router'

Vue.config.productionTip = false

new Vue({
  axios,
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
