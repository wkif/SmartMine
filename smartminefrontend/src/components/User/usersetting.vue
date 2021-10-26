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
    <div style="background: #f0f2f5; padding: 30px">
      <a-card class="cardView">
        <a-row>
          <a-col :span="3">
            <a-menu
              style="width: 100%"
              :default-selected-keys="['1']"
              mode="inline"
            >
              <a-menu-item key="1">
                <router-link to="/index/usersetting/Basicsetting">
                  <span>基本设置</span>
                </router-link>
              </a-menu-item>
              <a-menu-item key="2">
                <router-link to="/index/usersetting/securitySettings">
                  <span>安全设置</span>
                </router-link>
              </a-menu-item>
              <a-menu-item key="3">
                <router-link to="/index/usersetting/accountBinding">
                  <span>账号绑定</span>
                </router-link>
              </a-menu-item>
            </a-menu>
          </a-col>
          <a-col :span="21">
            <router-view />
          </a-col>
        </a-row>
      </a-card>
    </div>
  </div>
</template>

<script>
export default {
  props: {},
  components: {},
  data() {
    return {
      basePath: "/index",
      routes: [
        {
          path: "home",
          breadcrumbName: "首页",
        },
        {
          path: "usersetting",
          breadcrumbName: "个人设置",
        },
      ],
    };
  },
  methods: {},
};
</script>

<style lang="less" scoped>
.cardView {
  margin-left: 200px;
  margin-right: 200px;
}
</style>