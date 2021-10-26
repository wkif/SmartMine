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
    Energy_consumption_management
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
          path: "Energy_consumption_management",
          breadcrumbName: "能耗管理",
        },
      ],
    };
  },
  methods: {},
};
</script>

<style lang="less" scoped>
</style>