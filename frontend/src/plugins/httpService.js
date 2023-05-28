import axios from 'axios'
const httpServicePlugin = {
  install(Vue) {
    Vue.prototype.$axios = axios

    Vue.prototype.$setupAxios = function () {
      this.$axios.defaults.baseURL = process.env.VUE_APP_BASE
      this.$axios.defaults.headers['Content-Type'] = 'application/json'
      const token = localStorage.getItem('token')
      if(token) {
        Vue.prototype.$axios.defaults.headers.common['Authorization'] = token
      }
    }
  }
};

export default httpServicePlugin;