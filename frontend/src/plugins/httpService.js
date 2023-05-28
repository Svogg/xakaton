import axios from 'axios'
const httpServicePlugin = {
  install(Vue) {
    Vue.prototype.$axios = axios

    Vue.prototype.$setupAxios = function () {
      this.$axios.defaults.baseURL = process.env.VUE_APP_BASE
      this.$axios.defaults.headers['Content-Type'] = 'application/json'
      // this.$axios.interceptors.request.use(req => {
      //   req.headers['Authorization'] = `Bearer ${accessToken}`
      //   return req;
      // });
    }
  }
};

export default httpServicePlugin;