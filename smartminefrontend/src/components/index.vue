<template>
  <a-layout id="components-layout-demo-fixed">
    <a-layout-header :style="{ position: 'fixed', zIndex: 1, width: '100%' }">
      <div class="logo">kif</div>
      <a-menu
        :theme="theme"
        mode="horizontal"
        :default-selected-keys="['1']"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item key="1">
          <router-link to="/index/home">
            <a-icon type="home" />
            <span>首页</span>
          </router-link>
        </a-menu-item>
        <a-menu-item key="2">
          <router-link to="/index/production_management">
            <a-icon type="dashboard" />
            <span>生产管理</span>
          </router-link>
        </a-menu-item>
        <a-menu-item key="3">
          <router-link to="/index/Scheduling_control">
            <a-icon type="play-square" />
            <span>调度管理</span>
          </router-link>
        </a-menu-item>
        <a-menu-item key="4" v-if="admin">
          <router-link to="/index/Personnel_management">
            <a-icon type="user" />
            <span>人力资源管理</span>
          </router-link>
        </a-menu-item>
        <a-menu-item key="5">
          <router-link to="/index/Equipment_management">
            <!-- <a-icon type="user" /> -->
            <i class="iconfont icon-fuwuqishebei"></i>
            <span>设备管理</span>
          </router-link>
        </a-menu-item>

        <a-menu-item key="6">
          <router-link to="/index/safety_management">
            <a-icon type="alert" />
            <span>安全管理</span>
          </router-link>
        </a-menu-item>

        <a-menu-item key="7">
          <router-link to="/index/Energy_consumption_management">
            <a-icon type="alert" />
            <span>能耗管理</span>
          </router-link>
        </a-menu-item>

        <a-menu-item key="8">
          <router-link to="/index/Resource_reserve_management">
            <a-icon type="alert" />
            <span>资源储量管理</span>
          </router-link>
        </a-menu-item>

        <a-menu-item key="9">
          <router-link to="/index/System_Settings">
            <a-icon type="setting" />
            <span>系统设置</span>
          </router-link>
        </a-menu-item>

        <a-menu-item class="avatar">
          <a-switch
            default-checked
            checked-children="dark"
            un-checked-children="light"
            @change="changeTheme"
          />
        </a-menu-item>
        <a-menu-item class="language">
          <a-dropdown>
            <a class="ant-dropdown-link" @click="(e) => e.preventDefault()">
              <a-icon type="global" />
            </a>
            <a-menu slot="overlay">
              <a-menu-item>
                <a href="javascript:;">简体中文</a>
              </a-menu-item>
              <a-menu-item>
                <a href="javascript:;">繁体中文</a>
              </a-menu-item>
              <a-menu-item>
                <a href="javascript:;">English</a>
              </a-menu-item>
            </a-menu>
          </a-dropdown>
        </a-menu-item>
        <a-menu-item class="avatar">
          <a-dropdown>
            <a class="ant-dropdown-link">
              <a-avatar :src="avatar" />&nbsp;&nbsp;&nbsp;{{ username }}</a
            >
            <a-menu slot="overlay">
              <a-menu-item key="0">
                <router-link to="/index/userinfo">账号中心</router-link>
              </a-menu-item>
              <a-menu-item key="1">
                <router-link to="/index/usersetting/Basicsetting"
                  >账号设置</router-link
                >
              </a-menu-item>
              <a-menu-divider />
              <a-menu-item key="3" @click="loginout()"> 退出登录 </a-menu-item>
            </a-menu>
          </a-dropdown>
        </a-menu-item>
      </a-menu>
    </a-layout-header>
    <a-layout-content :style="{ padding: '0 20px', marginTop: '104px' }">
      <div :style="{ background: '#fff', padding: '24px', minHeight: '680px' }">
        <!-- 子页面展示部分 -->
        <router-view />
      </div>
    </a-layout-content>
    <template>
      <div id="components-back-top-demo-custom">
        <a-back-top>
          <div class="ant-back-top-inner">UP</div>
        </a-back-top>
      </div>
    </template>
    <a-layout-footer :style="{ textAlign: 'center' }">
      Design ©2021 Created by kif
    </a-layout-footer>
  </a-layout>
</template>
<style>
#components-layout-demo-fixed .logo {
  width: 120px;
  height: 31px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px 24px 16px 0;
  float: left;
}
.avatar {
  float: right;
}
.language {
  float: right;
}
#components-back-top-demo-custom .ant-back-top {
  bottom: 50px;
}
#components-back-top-demo-custom .ant-back-top-inner {
  height: 40px;
  width: 40px;
  line-height: 40px;
  border-radius: 4px;
  background-color: #1088e9;
  color: #fff;
  text-align: center;
  font-size: 20px;
}
.ant-layout-header {
  background: white;
}
</style>

<script>
export default {
  name: "index",
  props: {},
  components: {},
  data() {
    return {
      username: "",
      avatar: "",
      theme: "dark",
      admin: false,
    };
  },
  created() {
    let infoObject = JSON.parse(localStorage.getItem("userInfo"));
    this.username = infoObject.username;
    this.avatar = infoObject.avatar;
    console.log(infoObject)
    if (
      infoObject.user_type == "一级管理" ||
      infoObject.user_type == "二级管理"
    ) {
      this.admin = true;
    }
  },
  methods: {
    loginout: function () {
      //清空token
      window.sessionStorage.clear();
      window.localStorage.clear();
      //跳转到登录页
      this.$router.push("/");
    },
    changeTheme(checked) {
      this.theme = checked ? "dark" : "light";
    },
  },
};
</script>