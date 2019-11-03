import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import axios from 'axios'
import router from "@/router";

Vue.prototype.$http = axios
Vue.prototype.$baseURI = "http://localhost:8000/polls/";
Vue.config.productionTip = false

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
