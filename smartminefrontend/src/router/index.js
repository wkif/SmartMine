import Vue from 'vue'
import Router from 'vue-router'
import guide from '@/components/guide'
import login from '@/components/login'
import index from '@/components/index'
import home from '@/components/home/home'
import production_management from '@/components/production_management/production_management'
import Scheduling_control from '@/components/Scheduling_control/schedulingControl'

import Personnel_management from '@/components/Personnel_management/Personnel_management'
import alluser from '@/components/Personnel_management/alluser'
import Attendance_management from '@/components/Personnel_management/Attendance_management'


import userinfo from '@/components/User/userinfo'
import usersetting from '@/components/User/usersetting'
import basicSetting from '@/components/User/basicSetting'
import securitySettings from '@/components/User/securitySettings'
import accountBinding from '@/components/User/accountBinding'


import Equipment_management from '@/components/Equipment_management/Equipment_management'
import safety_management from '@/components/safety_management/safety_management'
import Energy_consumption_management from '@/components/Energy_consumption_management/Energy_consumption_management'
import Resource_reserve_management from '@/components/Resource_reserve_management/Resource_reserve_management'
import System_Settings from '@/components/System_Settings/System_Settings'


Vue.use(Router)

const router = new Router({
  routes: [{
      path: '/',
      name: 'guide',
      component: guide
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },

    {
      path: '/index',
      name: 'index',
      component: index,
      children: [ // 嵌套子路由
        {
          path: 'home',
          component: home
        },
        {
          path: 'production_management',
          component: production_management
        },
        {
          path: 'Scheduling_control',
          component: Scheduling_control
        },
        {
          path: 'Personnel_management',
          component: Personnel_management

        },


        {
          path: 'Equipment_management',
          component: Equipment_management
        },
        {
          path: 'safety_management',
          component: safety_management
        },
        {
          path: 'Energy_consumption_management',
          component: Energy_consumption_management
        },
        {
          path: 'Resource_reserve_management',
          component: Resource_reserve_management
        },
        {
          path: 'System_Settings',
          component: System_Settings
        },


        {
          path: 'alluser',
          component: alluser
        },
        {
          path: 'Attendance_management',
          component: Attendance_management
        },

        {
          path: 'userinfo',
          component: userinfo
        },
        {
          path: 'usersetting',
          component: usersetting,
          name: 'usersetting',
          children: [{
              path: 'basicSetting',
              component: basicSetting
            },
            {
              path: 'securitySettings',
              component: securitySettings
            },
            {
              path: 'accountBinding',
              component: accountBinding
            }
          ]
        },

      ]

    }
  ]
})
// 挂载
router.beforeEach((to, from, next) => {
  // to将要访问的路径
  // from 代表从哪个路径跳转而来
  // next是一个函数，表示放行
  // next()放行   next(' /login')强制跳转 

  if (to.path === '/') return next()
  if (to.path === '/login') return next()
  const tokenStr = window.sessionStorage.getItem("JWT_TOKEN")
  if (!tokenStr) return ("/login")
  next()

})
export default router
