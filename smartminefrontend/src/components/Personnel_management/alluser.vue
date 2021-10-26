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
    <!-- <template>
      <div style="background-color: #ececec; padding: 20px">
        <a-row :gutter="16">
          <a-col :span="8">
            <a-card title="总人数" :bordered="false">
              <p>{{ usernumber }}</p>
            </a-card>
            <br />
            <a-card title="部门" :bordered="false">
              <p>{{ usernumber }}</p>
            </a-card>
            <br />
            <a-card title="总人数" :bordered="false">
              <p>{{ usernumber }}</p>
            </a-card>
          </a-col>
          <a-col :span="16">
            <a-card title="人员分析" :bordered="false">
              <div style="background-color: #ececec">
                <div
                  style="width: auto; height: 600px"
                  id="User_analysis_table"
                ></div>
              </div>
            </a-card>
          </a-col>
        </a-row>
      </div>
    </template> -->

    <br />
    <br />
    <template>
      <div>
        <a-button type="primary" class="editable-add-btn" @click="adduser">
          添加人员
        </a-button>
        <a-button
          type="primary"
          class="editable-add-btn"
          @click="adduserbyFile"
        >
          批量导入人员
        </a-button>
        <a-table bordered :data-source="dataSource" :columns="columns">
          <span slot="id" slot-scope="id">
            <a-tag color="#D4AD76">
              {{ id }}
            </a-tag>
          </span>

          <span slot="age" slot-scope="age">
            <a-statistic :value="age" style="margin-right: 50px"> </a-statistic>
          </span>

          <span slot="gender" slot-scope="gender">
            <a-tag v-if="gender == '女'" color="pink">
              {{ gender }}
            </a-tag>

            <a-tag v-else color="blue">
              {{ gender }}
            </a-tag>
          </span>

          <span slot="device_type" slot-scope="device_type">
            <a-tag
              color="#108ee9"
              v-for="(type, key) in device_type"
              :key="key"
            >
              {{ type }}
            </a-tag>
          </span>
          <span slot="phone" slot-scope="phone">
            <a-statistic
              title="Tel"
              :value="phone"
              style="margin-right: 50px"
            />
          </span>
          <span slot="user_type" slot-scope="user_type">
            <a-tag v-if="user_type == '一级管理'" color="#f50">
              {{ user_type }}
            </a-tag>
            <a-tag v-else-if="user_type == '二级管理'" color="#2db7f5">
              {{ user_type }}
            </a-tag>
            <a-tag v-else color="#87d068">
              {{ user_type }}
            </a-tag>
          </span>

          <template slot="operation" slot-scope="text, record">
            <a-popconfirm
              v-if="dataSource.length"
              title="删除该用户?"
              @confirm="() => onDelete(record.id)"
            >
              <a href="javascript:;">删除</a>
            </a-popconfirm>
            <a-divider type="vertical" />
            <a-button type="link" @click="editUser(record)"> 编辑 </a-button>
            <a-divider type="vertical" />
            <a-button type="link" @click="Equipment_permissions(record)">
              设备权限
            </a-button>
            <a-divider type="vertical" />
            <a-button type="link" @click="gotouserInfo(record.id)">
              查看
            </a-button>
          </template>
        </a-table>
      </div>
    </template>

    <a-modal
      title="添加人员"
      :visible="visible_adduser"
      :confirm-loading="confirmLoading"
      @ok="handleSubmit"
      @cancel="handleCancel"
    >
      <a-form :form="form" :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }">
        <a-form-item label="姓名">
          <a-input
            v-decorator="[
              'realname',
              {
                rules: [
                  { required: true, message: 'Please input your realname!' },
                ],
              },
            ]"
          />
        </a-form-item>
        <a-form-item label="电话">
          <a-input
            v-decorator="[
              'phone',
              {
                rules: [
                  {
                    required: true,
                    message: 'Please input your phone number!',
                  },
                ],
              },
            ]"
            style="width: 100%"
          >
            <a-select
              slot="addonBefore"
              v-decorator="['prefix', { initialValue: '86' }]"
              style="width: 70px"
            >
              <a-select-option value="86"> +86 </a-select-option>
              <a-select-option value="87"> +87 </a-select-option>
            </a-select>
          </a-input>
        </a-form-item>
        <a-form-item label="性别">
          <a-select
            v-decorator="[
              'gender',
              {
                rules: [
                  { required: true, message: 'Please select your gender!' },
                ],
              },
            ]"
            placeholder="Select a option and change input text above"
          >
            <a-select-option value="男"> 男 </a-select-option>
            <a-select-option value="女"> 女 </a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="用户权限级别">
          <a-select
            v-decorator="[
              'user_type',
              {
                rules: [
                  { required: true, message: 'Please select your user_type!' },
                ],
              },
            ]"
            placeholder="Select a option and change input text above"
          >
            <a-select-option value="一级管理"> 一级管理 </a-select-option>
            <a-select-option value="二级管理"> 二级管理 </a-select-option>
            <a-select-option value="普通员工"> 普通员工 </a-select-option>
          </a-select>
        </a-form-item>

      </a-form>
    </a-modal>
    <a-modal
      title="批量导入人员"
      width="60%"
      :visible="visible_adduserbyFile"
      :confirm-loading="confirmLoading_adduserbyFile"
      @ok="handleSubmit_adduserbyFile"
      @cancel="handleCancel_adduserbyFile"
    >
      <div class="">
        <a-upload
          style="display: flex; margin: 5px"
          name="file"
          :multiple="false"
          action="/"
          method="post"
          accept=".xls, .xlsx"
          :headers="headers"
          @change="readExcel"
          :showUploadList="false"
        >
          <!-- showUploadList是把文件list隐藏，我也不往后端存，单纯的解析数据，不需要操作list，最关键的是太丑了 -->
          <a-button size="small" type="sive">文件</a-button>
        </a-upload>
        <a-button size="small" type="sive" @click="downloadExecl"
          >下载模板</a-button
        >
        <a-table
          :columns="uploadColumns"
          :data-source="uploadData"
          :pagination="false"
        >
        </a-table>
      </div>
    </a-modal>

    <a-modal
      title="编辑"
      :visible="visible_editUser"
      :confirm-loading="confirmLoading_editUser"
      @ok="handleOk_editUser"
      @cancel="handleCancel_editUser"
      class="editusermodal"
    >
      <a-form :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }">
        <a-form-item label="姓名">
          <a-input
            v-decorator="[
              'realname',
              {
                rules: [
                  { required: true, message: 'Please input your realname!' },
                ],
              },
            ]"
            v-model="editform.realname"
          />
        </a-form-item>
        <a-form-item label="电话">
          <a-input
            v-decorator="[
              'phone',
              {
                rules: [
                  {
                    required: true,
                    message: 'Please input your phone number!',
                  },
                ],
              },
            ]"
            style="width: 100%"
            v-model="editform.phone"
          >
          </a-input>
        </a-form-item>

        <a-form-item label="年龄">
          <a-input
            v-decorator="[
              'age',
              {
                rules: [{ required: true, message: 'Please input your age!' }],
              },
            ]"
            v-model="editform.age"
          />
        </a-form-item>

        <a-form-item label="邮箱">
          <a-input
            v-decorator="[
              'userEmail',
              {
                rules: [
                  { required: true, message: 'Please input your userEmail!' },
                ],
              },
            ]"
            v-model="editform.userEmail"
          />
        </a-form-item>

        <a-form-item label="性别">
          <a-select
            v-decorator="[
              'gender',
              {
                rules: [
                  { required: true, message: 'Please select your gender!' },
                ],
              },
            ]"
            placeholder="Select a option and change input text above"
            v-model="editform.gender"
          >
            <a-select-option value="男"> 男 </a-select-option>
            <a-select-option value="女"> 女 </a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="用户级别">
          <a-select
            v-decorator="[
              'user_type',
              {
                rules: [
                  { required: true, message: 'Please select your user_type!' },
                ],
              },
            ]"
            placeholder="Select a option and change input text above"
            v-model="editform.user_type"
          >
            <a-select-option value="一级管理"> 一级管理 </a-select-option>
            <a-select-option value="二级管理"> 二级管理 </a-select-option>
            <a-select-option value="普通员工"> 普通员工 </a-select-option>
          </a-select>
        </a-form-item>
   
      </a-form>
    </a-modal>

    <!-- 设备权限modal----start -->
    <a-modal
      title="设备权限分配"
      :visible="visible_Equipment_permissions"
      :confirm-loading="confirmLoading_Equipment_permissions"
      @ok="handleOk_Equipment_permissions"
      @cancel="handleCancel_Equipment_permissions"
    >
      <div>
        <div :style="{ borderBottom: '1px solid #E9E9E9' }">
          <a-checkbox
            :indeterminate="indeterminate"
            :checked="checkAll"
            @change="onCheckAllChange"
          >
            Check all
          </a-checkbox>
        </div>
        <br />
        <a-checkbox-group
          v-model="checkedList"
          :options="plainOptions"
          @change="onChange"
        />
      </div>
    </a-modal>

    <!-- 设备权限modal----end -->
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
        {
          path: "alluser",
          breadcrumbName: "人员管理",
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
    };
  },

  methods: {
    onDelete(key) {
      if (key == JSON.parse(localStorage.getItem("userInfo")).id) {
        this.$message.error("不能删除当前登录账号");
      }
      var that = this;
      let Data = {
        id: key,
      };
      that.$axios.post("deleteuser/", Data).then(function (res) {
        if (res.data.status == 200) {
          that.$message.success(res.data.msg);
          that.getalluserData();
          that.get_device_type_Data();
          const dataSource = [...that.dataSource];
          that.dataSource = dataSource.filter((item) => item.id !== key);
        }
      });
    },
    editUser(key) {
      this.visible_editUser = true;
      console.log(key);
      this.editform = key;
    },
    handleOk_editUser() {
      this.confirmLoading_editUser = true;

      var that = this;
      let Data = that.editform;
      console.log(Data);
      that.$axios.post("edituserinfoBYadmin/", Data).then(function (res) {
        if (res.data.status == 200) {
          that.$message.success(res.data.msg);
          that.getalluserData();
          that.get_device_type_Data();
          that.visible_editUser = false;
          that.confirmLoading_editUser = false;
        }
      });
    },
    handleCancel_editUser() {
      this.visible_editUser = false;
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
    adduser() {
      this.visible_adduser = true;
    },

    handleCancel(e) {
      this.visible_adduser = false;
    },

    handleSubmit(e) {
      e.preventDefault();
      var that = this;
      that.form.validateFields((err, values) => {
        if (!err) {
          that.confirmLoading = true;
          let data = values;
          data.phone = data.prefix + data.phone;
          delete data.prefix;
          that.$axios.post("add_user/", data).then(function (res) {
            if (res.data.errorcode == 0) {
              that.visible_adduser = false;
              that.$message.success("添加成功");
              const { count, dataSource } = that;
              const newData = {
                id: count,
                username: ` `,
                realname: data.realname,
                age: "",
                gender: data.gender,
            
                phone: data.phone,
                userEmail: "",
                city: "",
                user_type: data.user_type,
              };
              that.dataSource = [...dataSource, newData];
              that.count = count + 1;
            } else {
              that.confirmLoading = false;
              that.$message.error(res.data.msg);
            }
          });
        }
      });
    },

    adduserbyFile() {
      this.visible_adduserbyFile = true;
    },
    handleCancel_adduserbyFile() {
      this.visible_adduserbyFile = false;
    },
    downloadExecl() {
      this.$axios
        .get("downloadxlsxdemo/", { responseType: "blob" })
        .then((response) => {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement("a");
          link.href = url;
          link.setAttribute("download", "demo.xlsx");
          document.body.appendChild(link);
          link.click();
        });
    },
    readExcel(files) {
      this.fileData = files; // 保存当前选择文件
      let that = this;
      let type = files.file.name.split(".");
      if (!files) {
        return false;
      } else if (
        type[type.length - 1] !== "xlsx" &&
        type[type.length - 1] !== "xls"
      ) {
        this.$message.error("上传格式不正确，请上传xls或者xlsx格式");
        return false;
      }
      const fileReader = new FileReader();
      // 如果为原生 input 则应是 files[0]
      fileReader.readAsBinaryString(files.file.originFileObj);
      fileReader.onload = (ev) => {
        // 异步执行
        try {
          const data = ev.target.result;
          const workbook = XLSX.read(data, {
            type: "binary",
          });
          const wsname = workbook.SheetNames[0]; //取第一张表
          const ws = XLSX.utils.sheet_to_json(workbook.Sheets[wsname]); //生成json表格内容
          that.uploadData = []; //清空接收数据
          for (var i = 0; i < ws.length; i++) {
            var sheetData = {
              // 键名为绑定 el 表格的关键字，值则是 ws[i][对应表头名]
              sort: i + 1,
              id: i,
              realname: ws[i]["姓名"],
              phone: ws[i]["电话"],
              gender: ws[i]["性别"],
              user_type: ws[i]["用户级别"],

            };
            that.uploadData.push(sheetData);
          }
        } catch (ev) {
          return false;
        }
      };
    },
    handleSubmit_adduserbyFile() {
      var that = this;
      this.confirmLoading_adduserbyFile = true;
      let succ = 0;
      let fail = 0;
      for (var i = 0; i < this.uploadData.length; i++) {
        let data = this.uploadData[i];
        setTimeout(
          that.$axios.post("add_user/", data).then(function (res) {
            console.log(res);
            if (res.data.status == "400") {
              fail++;
            } else {
              succ++;
            }
          }),
          1000
        );
      }
      setTimeout(
        ((this.visible_adduserbyFile = false),
        this.$message.success("成功导入" + succ + "项，失败" + fail + "项")),
        2000
      );
    },

    // handleSelectChange(value) {
    // },

 

    // 设备权限分配start
    Equipment_permissions(e) {
      console.log(e);
      this.userid = e.id;
      this.checkedList = e.device_type;
      this.visible_Equipment_permissions = true;
    },
    handleOk_Equipment_permissions() {
      this.confirmLoading = true;

      let Data = {
        device_type_namelist: this.checkedList,
        person_id: this.userid,
      };
      console.log(Data);
      var that = this;
      that.$axios.post("add_person_to_device/", Data).then(function (res) {
        if (res.data.errorcode == 0) {
          that.$message.success(res.data.content);
        } else {
          that.$message.error(res.data.msg);
        }
        that.visible_Equipment_permissions = false;
        that.confirmLoading_Equipment_permissions = false;
        that.getalluserData();
      });
    },
    handleCancel_Equipment_permissions() {
      this.visible_Equipment_permissions = false;
    },

    onChange(checkedList) {
      this.indeterminate =
        !!checkedList.length && checkedList.length < plainOptions.length;
      this.checkAll = checkedList.length === plainOptions.length;
    },
    onCheckAllChange(e) {
      Object.assign(this, {
        checkedList: e.target.checked ? plainOptions : [],
        indeterminate: false,
        checkAll: e.target.checked,
      });
    },
    get_device_type_Data() {
      var that = this;
      that.$axios.get("get_device_type_Data/").then(function (res) {
        if (res.data.status == 200) {
          // that.device_type_Data = res.data.info;
          for (var i = 0; i < res.data.info.length; i++) {
            plainOptions.push(res.data.info[i].name);
          }
        }
      });
    },
    // 设备权限分配end

    gotouserInfo(e) {
      console.log(e);
      this.$router.push({ path: "/index/userinfo?userid=" + e });
    },
  },
  mounted() {
    this.checkedList = [];
    this.defaultCheckedList = [];
    // this.User_analysis_table();
    this.getalluserData();
    this.get_device_type_Data();
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
</style>