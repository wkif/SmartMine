<template>
  <div>
    <div>
      <a-breadcrumb :routes="routes">
        <template slot="itemRender" slot-scope="{ route, routes, paths }">
          <span v-if="routes.indexOf(route) === routes.length - 1">
            {{ route.breadcrumbName }}
          </span>
          <router-link v-else :to="`${basePath}/${paths.join('/')}`">
            {{ route.breadcrumbName }}
          </router-link>
        </template>
      </a-breadcrumb>
      <br />
    </div>
    <div style="background-color: #ececec; padding: 20px; height: 100%">
      <a-row :gutter="16">
        <a-col :span="9">
          <a-card hoverable style="width: 100%">
            <a-card-meta :title="user.realname" :description="user.user_type">
              <a-avatar slot="avatar" :src="user.avatar" />
            </a-card-meta>
          </a-card>

          <a-card style="width: 100%">
            <p>
              <i class="iconfont icon-gerenyuangong"></i> {{ user.username }}
            </p>
            <p><a-icon type="phone" /> {{ user.phone }}</p>
            <p>
              <a-icon type="environment" /> {{ user.country }}.{{
                user.province
              }}.{{ user.city }}
            </p>
            <p><i class="iconfont icon-youjian1"></i> {{ user.userEmail }}</p>
            <p>
              <i class="iconfont icon-qiyegongsidalou"></i>
              {{ user.department }}
            </p>
          </a-card>
        </a-col>
        <a-col :span="15">
          <a-card
            style="width: 100%"
            :tab-list="tabListNoTitle"
            :active-tab-key="noTitleKey"
            @tabChange="(key) => onTabChange(key, 'noTitleKey')"
          >
            <p v-if="noTitleKey === '设备'">设备</p>
            <p v-else-if="noTitleKey === 'app'">app content</p>
            <p v-else>project content</p>
            <a slot="tabBarExtraContent" href="#">More</a>
          </a-card>
        </a-col>
      </a-row>
    </div>
  </div>
</template>

<script>
export default {
  props: {},
  components: {},
  data() {
    const { lang } = this.$route.params;
    return {
      user: {},

      tabListNoTitle: [
        {
          key: "设备",
          tab: "设备",
        },
        {
          key: "app",
          tab: "app",
        },
        {
          key: "project",
          tab: "project",
        },
      ],
      key: "tab1",
      noTitleKey: "app",
      basePath: "/index",
      routes: [
        {
          path: "home",
          breadcrumbName: "首页",
        },
        {
          path: "userinfo",
          breadcrumbName: "个人中心",
        },
      ],
    };
  },
  mounted() {
    let Data;
    if (this.$route.query.userid) {
      Data = {
        id: this.$route.query.userid,
      };
      var that = this;
      that.$axios.post("getuserinfo/", Data).then(function (res) {
        if (res.data.status == 400) {
          that.$message.error(res.data.msg);
        } else if (res.data.status == 200) {
          that.user = res.data.info;
        } else {
          that.$message.error("未知错误，请重试");
        }
      });
    } else {
      let infoObject = JSON.parse(localStorage.getItem("userInfo"));
      this.user = infoObject;
      Data = {
        id: infoObject.id,
      };
      var that = this;
      that.$axios.post("getuserinfo/", Data).then(function (res) {
        if (res.data.status == 400) {
          that.$message.error(res.data.msg);
        } else if (res.data.status == 200) {
          that.user = res.data.info;
          localStorage.setItem("userInfo", JSON.stringify(res.data.info));
        } else {
          that.$message.error("未知错误，请重试");
        }
      });
    }
  },
  methods: {
    onTabChange(key, type) {
      this[type] = key;
    },
  },
};
</script>

<style lang="less">
</style>