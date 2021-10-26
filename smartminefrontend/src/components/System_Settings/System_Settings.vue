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
    System_Settings
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
          path: "System_Settings",
          breadcrumbName: "系统设置",
        },
      ],
    };
  },
  methods: {},
};
</script>

<style lang="less" scoped>
</style>