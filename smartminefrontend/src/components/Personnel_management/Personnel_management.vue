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
    <template>
      <div style="background-color: #f0f2f5; padding: 20px">
        <a-row>
          <a-col :span="4">
            <a-card
              style="width: 200px; margin: 10px"
              hoverable="true"
              @click="gotoalluser()"
            >
              <a-icon type="contacts" />
              <p>人事管理</p>
            </a-card></a-col
          >
          <a-col :span="4">
            <a-card style="width: 200px; margin: 10px" hoverable="true">
              <a-icon type="account-book" />
              <p>薪酬管理</p>
            </a-card></a-col
          >
          <a-col :span="4">
            <a-card style="width: 200px; margin: 10px" hoverable="true"
              @click="gotoAttendance_management()">
              <a-icon type="carry-out" />
              <p>考勤管理</p>
            </a-card>
          </a-col>
          <a-col :span="4">
            <a-card style="width: 200px; margin: 10px" hoverable="true">
              <a-icon type="container" />
              <p>绩效管理</p>
            </a-card></a-col
          >
          <a-col :span="4">
            <a-card style="width: 200px; margin: 10px" hoverable="true">
              <a-icon type="funnel-plot" />
              <p>培训管理</p>
            </a-card>
          </a-col>
        </a-row>
        <a-row :gutter="16">
          <a-col :span="24">
            <a-card title="人事架构" :bordered="false">
              <div class="col-md-10 col-md-offset-1">
                <div class="oTree">
                  <vue2-org-tree
                    :data="Treedata"
                    :horizontal="horizontal"
                    :collapsable="collapsable"
                    :render-content="renderContent"
                    @on-expand="onExpand"
                    @on-node-click="onNodeClick"
                  />
                </div>
              </div>
            </a-card>
          </a-col>
        </a-row>
        <a-card title="人员分析" :bordered="false">
          <div style="background-color: #ececec; padding: 20px">
            <div
              style="width: auto; height: 600px"
              id="User_analysis_table"
            ></div>
          </div>
        </a-card>
      </div>
    </template>

    <br />
    <br />
  </div>
</template>




<script>
import XLSX from "xlsx";
import * as echarts from "echarts";
import "echarts-gl";
const plainOptions = [];
const defaultCheckedList = [];
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
          path: "Personnel_management",
          breadcrumbName: "人力资源管理",
        },
      ],
      dataSource: [],
      usernumber: "",
      count: 2,
      columns: [
        {
          title: "id",
          dataIndex: "id",
          scopedSlots: { customRender: "id" },
        },
        {
          title: "用户名",
          dataIndex: "username",
          scopedSlots: { customRender: "username" },
        },
        {
          title: "姓名",
          dataIndex: "realname",
          scopedSlots: { customRender: "realname" },
        },
        {
          title: "年龄",
          dataIndex: "age",
          scopedSlots: { customRender: "age" },
        },
        {
          title: "性别",
          dataIndex: "gender",
          scopedSlots: { customRender: "gender" },
        },
        {
          title: "部门",
          dataIndex: "department",
        },
        {
          title: "电话",
          dataIndex: "phone",
          scopedSlots: { customRender: "phone" },
        },
        {
          title: "邮箱",
          dataIndex: "userEmail",
        },
        {
          title: "城市",
          dataIndex: "city",
        },
        {
          title: "用户级别",
          dataIndex: "user_type",
          scopedSlots: { customRender: "user_type" },
        },
        {
          title: "设备权限",
          dataIndex: "device_type",
          scopedSlots: { customRender: "device_type" },
        },

        {
          title: "操作",
          dataIndex: "operation",
          width: "21%",
          scopedSlots: { customRender: "operation" },
        },
      ],
      visible_adduser: false,
      confirmLoading: false,

      visible_adduserbyFile: false,
      confirmLoading_adduserbyFile: false,

      visible_editUser: false,
      confirmLoading_editUser: false,

      form: this.$form.createForm(this, { name: "coordinated" }),
      // piliang
      uploadData: [], //文件数据
      fileData: "", // 保存选择的文件
      //上传文件请求头,我这个没走后端，没啥用，姑且放这吧
      headers: {
        authorization: "authorization-text",
      },
      uploadColumns: [
        {
          dataIndex: "id",
          key: "id",
          title: "序号",
        },
        {
          dataIndex: "realname",
          key: "realname",
          title: "姓名",
        },
        {
          dataIndex: "phone",
          key: "phone",
          title: "手机号",
        },

        {
          dataIndex: "gender",
          key: "gender",
          title: "性别",
        },
        {
          dataIndex: "user_type",
          key: "user_type",
          title: "级别",
        },
        {
          dataIndex: "department",
          key: "department",
          title: "部门",
        },
      ],
      // 数据分析
      department: "",

      // 设备权限分配strat
      visible_Equipment_permissions: false,
      confirmLoading_Equipment_permissions: false,
      userid: "",

      checkedList: defaultCheckedList,
      indeterminate: true,
      checkAll: false,
      plainOptions,
      device_type_Data: [],

      // 设备权限分配end
      // edit start
      editform: [],
      // edit end

      // 架构图

      // 测试数据
      Treedata: {
        id: 0,
        label: "开发科技",
        children: [
          {
            id: 2,
            label: "技术部",
            children: [
              {
                id: 5,
                label: "前端部门",
                children: [
                  {
                    id: 10,
                    label: "小谢",
                  },
                  {
                    id: 11,
                    label: "小于",
                  },
                  {
                    id: 12,
                    label: "小菜",
                  },
                ],
              },
              {
                id: 6,
                label: "后端部门",
                children: [
                  {
                    id: 12,
                    label: "小胡",
                  },
                  {
                    id: 12,
                    label: "小向",
                  },
                ],
              },
              {
                id: 9,
                label: "UI设计",
                children: [
                  {
                    id: 15,
                    label: "小魏",
                  },
                ],
              },
              {
                id: 10,
                label: "测试部门",
                children: [
                  {
                    id: 16,
                    label: "小张",
                  },
                ],
              },
            ],
          },
          {
            id: 3,
            label: "项目部",
            children: [
              {
                id: 7,
                label: "项目一部",
                children: [
                  {
                    id: 17,
                    label: "负责人",
                  },
                ],
              },
              {
                id: 8,
                label: "项目二部",
                children: [
                  {
                    id: 18,
                    label: "负责人",
                  },
                  {
                    id: 19,
                    label: "负责人",
                  },
                ],
              },
            ],
          },
          {
            id: 4,
            label: "测绘部",
            children: [
              {
                id: 13,
                label: "小料",
              },
              {
                id: 13,
                label: "小留",
              },
            ],
          },
          {
            id: 9,
            label: "人事部",
            children: [
              {
                id: 14,
                label: "笑笑",
              },
            ],
          },
        ],
      },
    };
  },

  methods: {
    gotoalluser() {
      this.$router.push("/index/alluser");
    },
    gotoAttendance_management(){
      this.$router.push("/index/Attendance_management");
    },

    getalluserData() {
      var that = this;
      that.$axios.get("getalluser/").then(function (res) {
        if (res.data.status == 200) {
          console.log(res.data.info);
          // for(var i =0;i<res.data.info.length;i++) {

          // }
          that.dataSource = res.data.info;
          length = that.dataSource.length;
          that.usernumber = length;
          that.count = that.dataSource[length - 1].id + 1;
        }
      });
    },

    // 数据分析
    User_analysis_table() {
      var chartDom = document.getElementById("User_analysis_table");
      var myChart = echarts.init(chartDom);
      var option;
      option = {
        tooltip: {
          trigger: "axis",
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: "shadow", // 默认为直线，可选为：'line' | 'shadow'
          },
        },
        legend: {
          data: [
            "性别",
            "男",
            "女",
            "管理",
            "一级管理",
            "二级管理",
            "普通成员",
          ],
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: [
          {
            type: "category",
            data: [
              "部门1",
              "部门2",
              "部门3",
              "部门4",
              "部门5",
              "部门6",
              "部门7",
            ],
          },
        ],
        yAxis: [
          {
            type: "value",
          },
        ],
        series: [
          {
            name: "性别",
            type: "bar",
            data: [34, 31, 29, 36, 38, 56, 52],
            emphasis: {
              focus: "series",
            },
            // markLine: {
            //   lineStyle: {
            //     type: "dashed",
            //   },
            //   data: [[{ type: "min" }, { type: "max" }]],
            // },
          },
          {
            name: "男",
            type: "bar",
            stack: "性别",
            emphasis: {
              focus: "series",
            },
            data: [12, 13, 10, 13, 9, 23, 21],
          },
          {
            name: "女",
            type: "bar",
            stack: "性别",
            emphasis: {
              focus: "series",
            },
            data: [22, 18, 19, 23, 29, 33, 31],
          },

          {
            name: "管理",
            type: "bar",
            data: [12, 13, 14, 15, 16, 17, 18],
            emphasis: {
              focus: "series",
            },
            // markLine: {
            //   lineStyle: {
            //     type: "dashed",
            //   },
            //   data: [[{ type: "min" }, { type: "max" }]],
            // },
          },
          {
            name: "一级管理",
            type: "bar",
            barWidth: 5,
            stack: "管理",
            emphasis: {
              focus: "series",
            },
            data: [4, 5, 6, 5, 4, 7, 9],
          },
          {
            name: "二级管理",
            type: "bar",
            stack: "管理",
            emphasis: {
              focus: "series",
            },
            data: [5, 4, 5, 5, 6, 5, 3],
          },
          {
            name: "普通成员",
            type: "bar",
            stack: "管理",
            emphasis: {
              focus: "series",
            },
            data: [3, 4, 3, 5, 6, 5, 6],
          },
        ],
      };

      option && myChart.setOption(option);
    },

    // 架构图
    renderContent(h, data) {
      return data.label;
    },
    // 节点点击展开/折叠（注意：参数e需要携带）
    onExpand(e, data) {
      if ("expand" in data) {
        data.expand = !data.expand;
        if (!data.expand && data.children) {
          this.collapse(data.children);
        }
      } else {
        this.$set(data, "expand", true);
      }
    },
    // 节点点击
    onNodeClick(e, data) {
      alert(data.label);
    },
    collapse(list) {
      var _this = this;
      list.forEach(function (child) {
        if (child.expand) {
          child.expand = false;
        }
        child.children && _this.collapse(child.children);
      });
    },
    // 是否全部展开
    expandChange() {
      this.toggleExpand(this.data, this.expandAll);
    },
    toggleExpand(data, val) {
      var _this = this;
      if (Array.isArray(data)) {
        data.forEach(function (item) {
          _this.$set(item, "expand", val);
          if (item.children) {
            _this.toggleExpand(item.children, val);
          }
        });
      } else {
        this.$set(data, "expand", val);
        if (data.children) {
          _this.toggleExpand(data.children, val);
        }
      }
    },
  },
  mounted() {
    this.checkedList = [];
    this.defaultCheckedList = [];
    this.User_analysis_table();
    this.getalluserData();
    // this.get_device_type_Data();
  },
};
</script>

<style lang="less" scoped>
.editable-cell {
  position: relative;
}

.editable-cell-input-wrapper,
.editable-cell-text-wrapper {
  padding-right: 24px;
}

.editable-cell-text-wrapper {
  padding: 5px 24px 5px 5px;
}

.editable-cell-icon,
.editable-cell-icon-check {
  position: absolute;
  right: 0;
  width: 20px;
  cursor: pointer;
}

.editable-cell-icon {
  line-height: 18px;
  display: none;
}

.editable-cell-icon-check {
  line-height: 28px;
}

.editable-cell:hover .editable-cell-icon {
  display: inline-block;
}

.editable-cell-icon:hover,
.editable-cell-icon-check:hover {
  color: #108ee9;
}

.editable-add-btn {
  margin-bottom: 8px;
}

// 架构图
.oTree {
  margin-top: 50px;
  text-align: center;
  width: 100%;
  height: 100%;
}

.oTree .org-tree-node-label-inner {
  white-space: nowrap;
  background-color: white;
  border-radius: 5px;
  padding: 10px 20px;
  border: 2px #ccc solid;
}
</style>