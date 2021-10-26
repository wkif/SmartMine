<template>
  <div>
    <!-- form section start -->
    <section class="w3l-workinghny-form">
      <!-- /form -->
      <div class="workinghny-form-grid">
        <div class="wrapper">
          <div class="logo">
            <h1>
              <a class="brand-logo" href="index.html"
                ><span>登</span> 录</a
              >
            </h1>
            <!-- if logo is image enable this   
                        <a class="brand-logo" href="#index.html">
                            <img src="image-path" alt="Your logo" title="Your logo" style="height:35px;" />
                        </a> -->
          </div>
          <div class="workinghny-block-grid">
            <div class="workinghny-left-img align-end">
              <img
                src="../assets/images/2.png"
                class="img-responsive"
                alt="img"
              />
            </div>
            <div class="form-right-inf">
              <div class="login-form-content">
                <!-- <h2>Where to?</h2> -->
                <!-- <form action="#" class="signin-form" method="post"> -->
                <div class="one-frm">
                  <label>用户名或邮箱（username/Email）</label>
                  <input
                    type="text"
                    name="Name"
                    placeholder=""
                    required=""
                    v-model="username"
                  />
                </div>
                <div class="one-frm">
                  <label>密码（password）</label>
                  <input
                    type="password"
                    name="Password"
                    placeholder=""
                    required=""
                    v-model="password"
                  />
                </div>
                <!-- <label class="check-remaind">
                    <input type="checkbox" />
                    <span class="checkmark"></span>
                    <p class="remember">Remember Me</p>
                  </label> -->
                <button class="btn btn-style mt-3" @click="login()">
                  登录
                </button>
                <!-- <p class="already">
                    Don't have an account? <a href="#signin">Sign Up</a>
                  </p> -->
                <!-- </form> -->
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- //form -->
      <!-- copyright-->
      <div class="copyright text-center">
        <div class="wrapper">
          <p class="copy-footer-29">
            © 2020 Working Sign In. All rights reserved | Design by
            <!-- <a href="https://w3layouts.com">W3layouts</a> -->
          </p>
        </div>
      </div>
      <!-- //copyright-->
    </section>
    <!-- //form section start -->
  </div>
</template>

<script>
import "../assets/css/login.css";
import Vue from 'vue'     //注意，要在这个页面中引入vue，不然下面的Vue.prototype会报错
export default {
  props: {},
  components: {},
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    login: function () {
      let Data = {
        username: this.username,
        password: this.password,
      };
      var that = this;
      that.$axios.post("login/", Data).then(function (res) {

        if (res.data.status == 400) {
          that.$message.error(res.data.msg);
        } else if (res.data.status == 200) {
          that.$message.success("登陆成功");
          sessionStorage.setItem("JWT_TOKEN", res.data.token);
          localStorage.setItem("userInfo", JSON.stringify(res.data.info));
          // 全局变量$userMsg
          Vue.prototype.$userMsg = res.data.info;
          that.$router.push("/index/home");
        } else {
          that.$message.error("未知错误，请重试");
        }
      });
    },
  },
};
</script>

<style lang="less">
</style>