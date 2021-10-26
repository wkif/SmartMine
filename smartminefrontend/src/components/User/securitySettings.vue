<template>
  <div>
    <a-card>
      <p
        style="
          fontsize: 14px;
          color: rgba(0, 0, 0, 0.85);
          marginbottom: 16px;
          fontweight: 500;
        "
      >
        安全设置
      </p>

      <a-card title="账户密码">
        <a slot="extra" @click="changepassword">修改</a>
        当前密码强度：强
      </a-card>
      <a-card title="密保手机">
        <a slot="extra" @click="changephone">修改</a>
        已经绑定手机：{{ user.phone }}
      </a-card>
      <a-card title="邮箱">
        <a slot="extra" @click="changeEmail">修改</a>
        邮箱: {{ user.userEmail }}
      </a-card>
    </a-card>

    <!-- modal -->
    <a-modal
      title="修改密码"
      :visible="visible_changepassword"
      :confirm-loading="confirmLoading_changepassword"
      @ok="handleOk_changepassword"
      @cancel="handleCancel_changepassword"
    >
      <template>
        <a-form-model
          class="passwordform"
          layout="inline"
          :model="passwordForm"
        >
          <a-form-model-item>
            <a-input-password
              v-model="passwordForm.passwordLast"
              placeholder="原密码"
            >
              <a-icon
                slot="prefix"
                type="lock"
                style="color: rgba(0, 0, 0, 0.25)"
              />
            </a-input-password>
          </a-form-model-item>
          <br />
          <a-form-model-item>
            <a-input-password
              v-model="passwordForm.password1"
              placeholder="新密码"
            >
              <a-icon
                slot="prefix"
                type="lock"
                style="color: rgba(0, 0, 0, 0.25)"
              />
            </a-input-password>
          </a-form-model-item>
          <br />
          <a-form-model-item>
            <a-input-password
              v-model="passwordForm.password2"
              placeholder="重复新密码"
            >
              <a-icon
                slot="prefix"
                type="lock"
                style="color: rgba(0, 0, 0, 0.25)"
              />
            </a-input-password>
          </a-form-model-item>
        </a-form-model>
      </template>
    </a-modal>

    <a-modal
      title="修改邮箱"
      :visible="visible_changeEmail"
      :confirm-loading="confirmLoading_changeEmail"
      @ok="handleOk_changeEmail"
      @cancel="handleCancel_changeEmail"
    >
      <a-form layout="horizontal">
        <a-form-item
          label="邮箱"
          :label-col="formItemLayout.labelCol"
          :wrapper-col="formItemLayout.wrapperCol"
        >
          <a-input-search
            placeholder="input search text"
            :enter-button="buttoncontent"
            :disabled="!canClick"
            size="large"
            v-model="email"
            @search="getcode"
          />
        </a-form-item>
        {{ buttoncontent }}
        <a-form-item
          label="验证码"
          :label-col="formItemLayout.labelCol"
          :wrapper-col="formItemLayout.wrapperCol"
        >
          <a-input v-model="code" placeholder="input placeholder" />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script>
export default {
  props: {},
  components: {},
  data() {
    return {
      user: "",
      passwordForm: {
        passwordLast: "",
        password1: "",
        password2: "",
        id: "",
        password: "",
      },
      visible_changepassword: false,
      confirmLoading_changepassword: false,

      // 修改邮箱---start
      visible_changeEmail: false,
      confirmLoading_changeEmail: false,
      email: "",
      code: "",
      buttoncontent: "发送验证码",
      totalTime: 60, //记录具体倒计时时间
      canClick: true, //添加canClick
      // 修改邮箱---end
    };
  },
  computed: {
    formItemLayout() {
      const { formLayout } = this;
      return formLayout === "horizontal"
        ? {
            labelCol: { span: 4 },
            wrapperCol: { span: 14 },
          }
        : {};
    },
    buttonItemLayout() {
      const { formLayout } = this;
      return formLayout === "horizontal"
        ? {
            wrapperCol: { span: 14, offset: 4 },
          }
        : {};
    },
  },
  methods: {
    changepassword() {
      this.visible_changepassword = true;
    },
    changephone() {
      console.log("changephone");
    },

    checkPassword(oValue) {
      for (var i = 0; i < nodes.length; i++) {
        nodes[i].className = "";
      }

      if (/\d/.test(oValue) && /[a-z]/.test(oValue) && /[A-Z]/.test(oValue)) {
        return 1;
      } else if (
        /^\d+$/.test(oValue) ||
        /^[A-Z]+$/.test(oValue) ||
        /^[a-z]+$/.test(oValue)
      ) {
        return 2;
      } else {
        return 3;
      }
    },
    handleOk_changepassword(e) {
      if (
        this.passwordForm.passwordLast == "" ||
        this.passwordForm.password1 == "" ||
        this.passwordForm.password2 == ""
      ) {
        this.$message.error("不能为空！");
      } else {
        if (this.passwordForm.password1 != this.passwordForm.password2) {
          this.$message.error("两次密码不一致！");
        } else {
          this.confirmLoading_changepassword = true;
          var that = this;
          that.passwordForm.id = that.user.id;
          that.passwordForm.password = that.passwordForm.password1;
          that.$axios
            .post("changepassword/", that.passwordForm)
            .then(function (res) {
              if (res.data.status == 400) {
                that.$message.error(res.data.msg);
                that.confirmLoading_changepassword = false;
              } else if (res.data.status == 200) {
                that.$message.success(res.data.msg);
                that.visible_changepassword = false;
                that.confirmLoading_changepassword = false;
                //清空token
                window.sessionStorage.clear();
                window.localStorage.clear();
                //跳转到登录页
                that.$router.push("/");
              } else {
                that.$message.error("未知错误，请重试");
                that.confirmLoading_changepassword = false;
              }
            });
        }
      }
    },
    handleCancel_changepassword(e) {
      this.visible_changepassword = false;
    },

    // 修改邮箱   start
    changeEmail() {
      this.visible_changeEmail = true;
    },
    getcode(e) {
      var email = e;
      var reg = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
      if (reg.test(email)) {
        if (!this.canClick) return; //改动的是这两行代码
        this.canClick = false;
        this.buttoncontent = this.totalTime + "s后重新发送";
        let clock = setInterval(() => {
          this.totalTime--;
          this.contbuttoncontentnt = this.totalTime + "s后重新发送";
          if (this.totalTime < 0) {
            clearInterval(clock);
            this.buttoncontent = "重新发送验证码";
            this.totalTime = 10;
            this.canClick = true; //这里重新开启
          }
        }, 1000);
        var that = this;
        that.$axios.post("changeEmail/", { email: email }).then(function (res) {
          if (res.data.status == 200) {
            that.$message.success(res.data.msg);
          } else {
            that.$message.error("未知错误，请重试");
          }
        });
      } else {
        this.$message.error("邮箱格式不正确");
      }
    },
    handleOk_changeEmail() {
      if (this.email != "") {
        this.confirmLoading_changeEmail = true;
        let Data = {
          id: JSON.parse(localStorage.getItem("userInfo")).id,
          email: this.email,
          code: this.code,
        };
        var that = this;
        that.$axios.post("getemailcode/", Data).then(function (res) {
          if (res.data.status == 200) {
            that.$message.success(res.data.msg);
            that.visible_changeEmail = false;
            that.confirmLoading_changeEmail = false;
            setTimeout(location.reload(), 2000);
          } else if (res.data.status == 400) {
            that.$message.error(res.data.msg);
          } else {
            that.$message.error("未知错误，请重试");
          }
        });
      }
      else{
        this.$message.error("请正确输入");
      }
    },
    handleCancel_changeEmail() {
      this.visible_changeEmail = false;
    },
    // 修改邮箱   end
  },

  mounted() {
    let infoObject = JSON.parse(localStorage.getItem("userInfo"));
    this.user = infoObject;
    infoObject.phone = infoObject.phone.replace(
      /(\d{3})\d{4}(\d{4})/,
      "$1****$2"
    );

    let Data = {
      id: infoObject.id,
    };
    var that = this;
    that.$axios.post("getuserinfo/", Data).then(function (res) {
      if (res.data.status == 400) {
        that.$message.error(res.data.msg);
      } else if (res.data.status == 200) {
        res.data.info.phone = res.data.info.phone.replace(
          /(\d{3})\d{4}(\d{4})/,
          "$1****$2"
        );
        that.user = res.data.info;
      } else {
        that.$message.error("未知错误，请重试");
      }
    });
  },
};
</script>

<style lang="less" scoped>
.passwordform {
  text-align: center;
  width: 100%;
}
</style>