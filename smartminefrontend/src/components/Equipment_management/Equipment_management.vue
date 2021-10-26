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

    <div style="background: #ececec; padding: 30px">
      <a-card :bordered="false" style="width: 100%">
        <a-row>
          <a-col :span="10">
            <div style="width: auto; height: 200px" id="device_type_Data"></div>
          </a-col>
          <a-col :span="10">
            <div style="width: auto; height: 200px" id="device_by_status"></div>
          </a-col>
          <a-col :span="4">
            <a-button-group>
              <a-button type="primary" @click="add_device_type">
                添加设备类型
              </a-button>
              <a-button @click="add_one_device">添加设备</a-button>
            </a-button-group>
            <!-- <a-button type="primary" @click="add_device_type"> 添加设备类型 </a-button>
            <a-button type="primary" @click="add_one_device"> 添加设备 </a-button> -->
          </a-col>
        </a-row>
      </a-card>
      <!-- 添加设备类型弹窗start -->
      <div class="add_device_type">
        <a-modal
          title="添加设备类型"
          :visible="visible_add_device_type"
          :confirm-loading="confirmLoading_add_device_type"
          @ok="handleOk_add_device_type"
          @cancel="handleCancel_add_device_type"
        >
          <p>
            <a-input
              v-model="add_device_type_name"
              placeholder="输入设备类型名称（如：卡车）"
            />
          </p>
        </a-modal>
      </div>
      <!-- 添加设备类型弹窗end -->
      <!-- 增加具体设备start -->
      <div class="add_one_device">
        <a-modal
          title="增加具体设备"
          :visible="visible_add_one_device"
          :confirm-loading="confirmLoading_add_one_device"
          @ok="handleOk_add_one_device"
          @cancel="handleCancel_add_one_device"
        >
          <div>
            <a-radio-group
              v-model="add_one_device_type"
              @change="onChange"
              v-for="(value, key) in device_type_Data"
              :key="key"
            >
              <a-radio-button :value="value.name">
                {{ value.name }}
              </a-radio-button>
            </a-radio-group>
          </div>
          <a-divider />
          <a-input
            v-model="add_one_device_Equipment_serial_number"
            placeholder="输入设备编号"
          />
        </a-modal>
      </div>

      <!-- 增加具体设备end -->
    </div>
    <template>
      <a-table :columns="columns" :data-source="all_device_Data">
        <span slot="status" slot-scope="status">
          <a-tag v-if="status == '正常'" color="green">
            {{ status }}
          </a-tag>
          <a-tag v-if="status == '故障'" color="red">
            {{ status }}
          </a-tag>
          <a-tag v-if="status == '维修中'" color="cyan">
            {{ status }}
          </a-tag>
        </span>
        <span slot="type" slot-scope="type">
          <a-tag color="#2db7f5">
            {{ type }}
          </a-tag>
        </span>

        <span slot="Running_state" slot-scope="Running_state">
          <a-tag v-if="Running_state == '运行中'" color="green">
            {{ Running_state }}
          </a-tag>
          <a-tag v-if="Running_state == '休息'" color="cyan">
            {{ Running_state }}
          </a-tag>
        </span>
        <span slot="action" slot-scope="text, record">
          <a-popconfirm
            title="删除该设备?"
            @confirm="() => onDelete(record.id)"
          >
            <a-button type="danger" size="small"> 删除 </a-button>
            <!-- <a href="javascript:;" style="">删除</a> -->
          </a-popconfirm>
          <a-divider type="vertical" />
          <!-- <a class="ant-dropdown-link"> More actions <a-icon type="down" /> </a> -->
        </span>
      </a-table>
    </template>
  </div>
</template>


<script>
import * as echarts from "echarts";
import "echarts-gl";
const columns = [
  {
    title: "id",
    dataIndex: "id",
    key: "id",
  },
  {
    title: "状态",
    dataIndex: "status",
    key: "status",
    scopedSlots: { customRender: "status" },
  },
  {
    title: "类型",
    dataIndex: "type",
    key: "type",
    scopedSlots: { customRender: "type" },
  },
  {
    title: "设备编号",
    dataIndex: "Equipment_serial_number",
    key: "Equipment_serial_number",
    scopedSlots: { customRender: "Equipment_serial_number" },
  },
  {
    title: "运行状态",
    dataIndex: "Running_state",
    key: "Running_state",
    scopedSlots: { customRender: "Running_state" },
  },
  {
    title: "Action",
    key: "action",
    scopedSlots: { customRender: "action" },
  },
];

const data = [];
export default {
  props: {},
  components: {},
  data() {
    return {
      basePath: "/adminHome",
      routes: [
        {
          path: "home",
          breadcrumbName: "首页",
        },
        {
          path: "Equipment_management",
          breadcrumbName: "设备管理",
        },
      ],
      all_device_Data: [],
      device_type_Data: [],
      data,
      columns,

      // 添加设备类型弹窗start
      visible_add_device_type: false,
      confirmLoading_add_device_type: false,
      add_device_type_name: "",
      // 添加设备类型弹窗end

      // 增加具体设备start
      visible_add_one_device: false,
      confirmLoading_add_one_device: false,
      add_one_device_type: "",
      add_one_device_Equipment_serial_number: "",
      // 增加具体设备end
    };
  },
  methods: {
    get_all_device() {
      var that = this;
      that.$axios.get("get_all_device/").then(function (res) {
        that.all_device_Data = res.data.info;
        var chartDom = document.getElementById("device_by_status");
        var myChart = echarts.init(chartDom);
        var option;
        option = {
          tooltip: {
            trigger: "item",
          },
          legend: {
            top: "5%",
            left: "center",
          },
          series: [
            {
              name: "设备类型",
              type: "pie",
              radius: ["40%", "70%"],
              avoidLabelOverlap: false,
              itemStyle: {
                borderRadius: 10,
                borderColor: "#fff",
                borderWidth: 2,
              },
              label: {
                show: false,
                position: "center",
              },
              emphasis: {
                label: {
                  show: true,
                  fontSize: "40",
                  fontWeight: "bold",
                },
              },
              labelLine: {
                show: false,
              },
              data: res.data.info2,
            },
          ],
        };

        option && myChart.setOption(option);
      });
    },
    get_device_type_Data() {
      var that = this;
      that.$axios.get("get_device_type_Data/").then(function (res) {
        that.device_type_Data = res.data.info;
        var chartDom = document.getElementById("device_type_Data");
        var myChart = echarts.init(chartDom);
        var option;
        option = {
          tooltip: {
            trigger: "item",
          },
          legend: {
            top: "5%",
            left: "center",
          },
          series: [
            {
              name: "设备类型",
              type: "pie",
              radius: ["40%", "70%"],
              avoidLabelOverlap: false,
              itemStyle: {
                borderRadius: 10,
                borderColor: "#fff",
                borderWidth: 2,
              },
              label: {
                show: false,
                position: "center",
              },
              emphasis: {
                label: {
                  show: true,
                  fontSize: "40",
                  fontWeight: "bold",
                },
              },
              labelLine: {
                show: false,
              },
              data: res.data.info,
            },
          ],
        };

        option && myChart.setOption(option);
        myChart.on("click", function (params) {
          //  var a = params.dataIndex
          console.log(params, "我被点击了");
        });
      });
    },
    onDelete(e) {
      let Data = { device_id: e };
      var that = this;
      that.$axios.post("delete_one_device/", Data).then(function (res) {
        if (res.data.status == 200) {
          that.$message.success(res.data.msg);
          that.get_all_device();
          that.get_device_type_Data();
          const all_device_Data = [...that.all_device_Data];
          that.all_device_Data = all_device_Data.filter(
            (item) => item.id !== e
          );
        } else {
          that.$message.error("未知错误，请重试");
        }
      });
    },

    // 添加设备类型弹窗start
    add_device_type() {
      this.visible_add_device_type = true;
    },
    handleOk_add_device_type() {
      this.confirmLoading_add_device_type = true;
      let Data = {
        name: this.add_device_type_name,
      };
      var that = this;
      that.$axios.post("add_device_type/", Data).then(function (res) {
        if (res.data.status == 400) {
          that.$message.error(res.data.msg);
        } else if (res.data.errorcode == 0) {
          that.get_device_type_Data();
          that.visible_add_device_type = false;
          that.confirmLoading_add_device_type = false;
        } else {
          that.$message.error("未知错误，请重试");
        }
      });
    },
    handleCancel_add_device_type() {
      this.visible_add_device_type = false;
    },
    // 添加设备类型弹窗end
    // 增加具体设备start
    add_one_device() {
      this.visible_add_one_device = true;
    },
    onChange(e) {
      console.log(this.add_one_device_type);
    },
    handleOk_add_one_device() {
      this.confirmLoading_add_one_device = true;
      let Data = {
        device_type_name: this.add_one_device_type,
        Equipment_serial_number: this.add_one_device_Equipment_serial_number,
      };
      var that = this;
      that.$axios.post("add_one_device/", Data).then(function (res) {
        if (res.data.status == 400) {
          that.$message.error(res.data.msg);
        } else if (res.data.errorcode == 0) {
          that.get_all_device();
          that.get_device_type_Data();
          that.confirmLoading_add_one_device = false;
          that.visible_add_one_device = false;
        } else {
          that.$message.error("未知错误，请重试");
        }
      });
    },
    handleCancel_add_one_device() {
      this.visible_add_one_device = false;
    },
    // 增加具体设备end
  },
  mounted() {
    this.get_all_device();
    this.get_device_type_Data();
  },
};
</script>

<style lang="less" scoped>
</style>