// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import less from 'less'
import $ from 'jquery';
import axios from "axios"
// 新增代码：引入全部组件及样式
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
import '../src/assets/css/iconfont.css'
// import VCharts from 'v-charts'
import * as echarts from 'echarts';
import 'echarts-gl'

import XLSX from 'xlsx/dist/xlsx.full.min.js'
import Vue2OrgTree from 'vue2-org-tree'
import 'vue2-org-tree/dist/style.css'


Vue.use(Vue2OrgTree)

// 全局变量
import global_msg from '../src/assets/js/global.js'
Vue.prototype.$global_msg = global_msg;

window.jQuery = $;
window.$ = $;
Vue.config.productionTip = false
Vue.use(less)
Vue.use(Antd);
// Vue.use(VCharts)
Vue.prototype.$echarts = echarts


axios.defaults.baseURL = "http://127.0.0.1:8000/api_v1/"; // 关键步骤–填写后台请求统一的地址
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'; //设置全局数据发送格式
axios.interceptors.request.use(
  config => {
    if (sessionStorage.JWT_TOKEN) { // 判断是否存在token，如果存在的话，则每个http header都加上token
      config.headers.Authorization = `${sessionStorage.JWT_TOKEN}`;
    }
    return config;
  },
  err => {
    return Promise.reject(err);
  });

Vue.config.productionTip = false;
Vue.prototype.$axios = axios;
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {
    App
  },
  template: '<App/>'
})
