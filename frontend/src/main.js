import Vue from 'vue'
import App from './App.vue'
import '@/styles/main.scss';
import vuetify from './plugins/vuetify'
import store from './store'
import router from './router'
import httpService from './plugins/httpService'

Vue.use(httpService)
Vue.config.productionTip = false

new Vue({
  vuetify,
  store,
  router,
  render: h => h(App)
}).$mount('#app')