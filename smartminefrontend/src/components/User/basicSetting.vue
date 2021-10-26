<template>
  <div>
    基本设置
    <a-row type="flex">
      <a-col flex="1 1 200px" class="basicsettingform">
        用户名
        <br />
        <br />
        <a-input placeholder="用户名" v-model="user.username" />
        <br />
        <br />
        年龄
        <br />
        <br />
        <a-input placeholder="年龄" v-model="user.age" />
        <br />
        <br />
        性别：
        <br />
        <br />
        <div>
          <a-radio-group v-model="user.gender" @change="onChange">
            <a-radio :style="radioStyle" value="男"> 男 </a-radio>
            <a-radio :style="radioStyle" value="女"> 女 </a-radio>
          </a-radio-group>
        </div>
        <br />
        <br />
        <a-button type="danger" @click="updatebasic"> 更新基本信息 </a-button>
      </a-col>
      <a-col flex="0 1 300px">
        <div @click="changeavatar">
          <img class="avatar" :src="user.avatar" />
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
export default {
  props: {},
  components: {},
  data() {
    return {
      user: "",
      radioStyle: {
        display: "block",
        height: "30px",
        lineHeight: "30px",
      },
    };
  },
  methods: {
    changeavatar() {
      console.log("changeavatar");
    },
    onChange(e) {
      console.log("radio checked", e.target.value);
    },
    updatebasic() {
      let data = {
        id: this.user.id,
        username: this.user.username,
        age: this.user.age,
        gender: this.user.gender,
      };
      var that = this;
      that.$axios.post("edituserinfo/", data).then(function (res) {
        if (res.data.status == 400) {
          that.$message.error(res.data.msg);
        } else if (res.data.status == 200) {
          localStorage.setItem("userInfo", JSON.stringify(res.data.info));
          that.$message.success(res.data.msg);
        } else {
          that.$message.error("未知错误，请重试");
        }
      });
    },
  },
  mounted() {
    let infoObject = JSON.parse(localStorage.getItem("userInfo"));
    this.user = infoObject;

    let Data = {
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
  },
};
</script>

<style lang="less" scoped>
.basicsettingform {
  padding: 20px;
}
.avatar {
  border-radius: 20%;
  width: 60%;
  height: 60%;
}
</style>