<template>
  <div>
    <!--header-->
    <header id="site-header" class="w3lhny-head fixed-top">
      <div class="container">
        <nav class="navbar navbar-expand-lg stroke px-0">
          <h1>
            <a class="navbar-brand" href="index.html">
              <span class="sublog"
                ><span
                  class="fa fa-industry w3llog-icon"
                  aria-hidden="true"
                ></span
                >智慧</span
              >矿山
            </a>
          </h1>
          <button
            class="navbar-toggler collapsed bg-gradient"
            type="button"
            data-toggle="collapse"
            data-target="#navbarTogglerDemo02"
            aria-controls="navbarTogglerDemo02"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon fa icon-expand fa-bars"></span>
            <span class="navbar-toggler-icon fa icon-close fa-times"></span>
          </button>

          <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
            <ul class="navbar-nav mx-lg-auto">
              <!-- <li class="nav-item active">
                <a class="nav-link" href="#"
                  >Home <span class="sr-only">(current)</span></a
                >
              </li>
              
              <li class="nav-item">
                <a class="nav-link" href="#">登录</a>
              </li> -->
            </ul>
          </div>
          <!-- toggle switch for light and dark theme -->
          <div class="mobile-position">
            <nav class="navigation">
              <!-- <div class="theme-switch-wrapper">
                <label class="theme-switch" for="checkbox">
                  <input type="checkbox" id="checkbox" />
                  <div class="mode-container">
                    <i class="gg-sun"></i>
                    <i class="gg-moon"></i>
                  </div>
                </label>
              </div> -->
              <button class="loginButton" @click="login()">登录</button>
            </nav>
          </div>
          <!-- //toggle switch for light and dark theme -->
        </nav>
      </div>
    </header>
    <!--/header-->
    <!-- main-slider -->
    <section id="intro" class="intro">
      <div class="container" style="display: flex">
        <div class="row Title">
          <div class="ti col-md-6 col-sm-8 col-xs-12">
            <div class="intro-content">
              <h1>智慧矿山-生产调度系统</h1>
              <p>
                专注于人工智能、大数据与虚拟现实技术，为全球矿业提供综合性智能化解决方案
              </p>
              <a
                class="btn btn-default scroll"
                href="#support"
                role="button"
                style="color: white"
                >了解我们 <i class="lnr lnr-arrow-down"></i
              ></a>
            </div>
          </div>
        </div>

        <div class="loginView"></div>
      </div>
    </section>
    <!-- /main-slider -->
    <!--/about-section -->
    <section class="w3l-index1 py-5" id="about">
      <div class="container py-lg-5 py-md-3">
        <div class="header-section text-center mx-0 mb-md-5 mb-4">
          <h6 class="title-subhny">智慧矿山概念</h6>
          <h3 class="title-w3l mt-2">
            以计算机网络系统、通信系统、控制系统等为数字化架构
          </h3>
        </div>
        <div class="row">
          <div class="col-lg-6 mb-lg-0 mb-md-5 mb-4 align-self">
            <!-- <h4 class="title-sub">研究领域</h4> -->
            <p class="mt-md-4 mt-3">
              在矿业资源管理、矿山开采、矿产采选加工处理等方面实现操作无人化、生产自动化、信息数字化。
              智慧矿山是在数字矿山基础上，通过对生产信息的智能化分析，实现矿山生产过程的智能化实时监控、管理与优化，最终建成现代智能化矿山。
            </p>
          </div>
          <div class="col-lg-6 pl-lg-5">
            <div class="position-relative">
              <img
                src="../assets/images/img1.jpg"
                alt=""
                class="radius-image img-fluid"
              />
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- //about-section -->
    <!-- home page block1 -->
    <section id="features" class="home-services py-5">
      <div class="container py-md-5 py-2">
        <div class="header-section text-center mx-0 mb-md-5 mb-4">
          <h6 class="title-subhny">Construction plan</h6>
          <h3 class="title-w3l mt-2">建设方案</h3>
        </div>
        <div class="row">
          <div class="col-lg-4 col-md-6 col-sm-12">
            <div class="box-wrap">
              <div class="box-wrap-grid">
                <div class="icon">
                  <span class="fa fa-cogs"></span>
                </div>
                <div class="info">
                  <h4><a href="#url">生产计划平台</a></h4>
                </div>
              </div>
              <p class="mt-3">
                露天矿中长期生产计划的编制是矿山生产工作中的重要环节,
                是指导和管理矿山正常生产的主要依据。
              </p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 col-sm-12 mt-md-0 mt-4">
            <div class="box-wrap">
              <div class="box-wrap-grid">
                <div class="icon">
                  <span class="fa fa-cubes"></span>
                </div>
                <div class="info">
                  <h4><a href="#url"> 生产调度平台</a></h4>
                </div>
              </div>
              <p class="mt-3">
                生产调度平台实现露天矿爆破作业中炸药的智能配比与卡车、铲车的智能调度。
              </p>
            </div>
          </div>
          <div class="col-lg-4 col-md-6 col-sm-12 mt-lg-0 mt-4">
            <div class="box-wrap">
              <div class="box-wrap-grid">
                <div class="icon">
                  <span class="fa fa-map-o"></span>
                </div>
                <div class="info">
                  <h4><a href="#url">系统监控平台</a></h4>
                </div>
              </div>
              <p class="mt-3">
                生产调度平台实现露天矿爆破作业中炸药的智能配比与卡车、铲车的智能调度。
              </p>
            </div>
          </div>
          <div class="col-lg-4 col-md-6 col-sm-12 mt-4">
            <div class="box-wrap">
              <div class="box-wrap-grid">
                <div class="icon">
                  <span class="fa fa-podcast"></span>
                </div>
                <div class="info">
                  <h4><a href="#url">安全预警监控平台</a></h4>
                </div>
              </div>
              <p class="mt-3">
                有效实现司机疲劳驾驶预警
                、自动避障辅助驾驶、低油位预警、低胎压报警、边坡不稳定预警和地质灾害预警，安全预警决策系统是矿山人员进行安全生产作业的有力保障。
              </p>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 col-sm-12 mt-4">
            <div class="box-wrap">
              <div class="box-wrap-grid">
                <div class="icon">
                  <span class="fa fa-podcast"></span>
                </div>
                <div class="info">
                  <h4><a href="#url">控制中心</a></h4>
                </div>
              </div>
              <p class="mt-3">
                大屏幕显示系统与电子地图相结合，能够直观体现系统运行状态，便于主控调度中心实时监测各生产阶段。
              </p>
            </div>
          </div>
          <div class="col-lg-4 col-md-6 col-sm-12 mt-4">
            <div class="box-wrap">
              <div class="box-wrap-grid">
                <div class="icon">
                  <span class="fa fa-podcast"></span>
                </div>
                <div class="info">
                  <h4><a href="#url">无人矿山规划</a></h4>
                </div>
              </div>
              <p class="mt-3">
                实现自主泊车、自适应巡航、自动避障等辅助驾驶功能，可以在一定程度上让驾驶员从枯燥繁琐的驾驶行为中解脱出来，为升级智慧矿山无人化奠定基础。
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- //home page block1 -->
    <section class="w3l-index2" id="about1">
      <div class="midd-w3 py-5">
        <div class="container py-lg-5 py-md-4 py-2">
          <div class="row">
            <div class="col-lg-6 left-wthree-img">
              <div class="position-relative">
                <img
                  src="../assets/images/img2.jpg"
                  alt=""
                  class="radius-image img-fluid"
                />
              </div>
            </div>
            <div class="col-lg-6 mt-lg-0 mt-5 pl-lg-5 align-self">
              <h6 class="title-subhny">特点</h6>
              <h3 class="title-w3l mt-2">
                数字矿山以计算机网络系统、通信系统、控制系统等为数字化架构
              </h3>
              <p class="mt-4">
                在矿业资源管理、矿山开采、矿产采选加工处理等方面实现
                操作无人化、生产自动化、信息数字化。智慧矿山是在数字矿山基础上，通过对生产信息的智能化分析，实现矿山生产过程的智能化实时监控、管理与优化，最终建成现代智能化矿山。
              </p>
              <ul class="w3l-right-book mt-4">
                <li>
                  <span class="fa fa-check" aria-hidden="true"></span>自主感知
                </li>
                <li>
                  <span class="fa fa-check" aria-hidden="true"></span>快速处理
                </li>
                <li>
                  <span class="fa fa-check" aria-hidden="true"></span>自主学习
                </li>
                <li>
                  <span class="fa fa-check" aria-hidden="true"></span>自动执行
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- home page block grids -->
    <!-- /content-6-section -->
    <section class="w3l-content-mid py-5">
      <!-- /content-6-section -->
      <div class="content-4-main py-3">
        <div class="container py-lg-4">
          <div class="welcome-left text-left">
            <h6 class="title-subhny mb-2">建设内容与目标</h6>
            <h3 class="title-w3l">针对矿山的实际地质条件和生产开采规划</h3>
            <p class="mt-3 mb-lg-2 pr-lg-5">
              结合特色专业背景，计划建设一套全覆盖的智慧矿山控制系统，特别针对现阶段矿山开采过程中的智能配矿编制、中长期计划编制问题中突遇不确定性因素、多目标动态卡铲调度系统、态势感知系统等难题提供专业全面的解决方案，
              同时对基于未来长远发展的无人矿山进行一个规划，基于“统一标准规范、统一数据资源、统一技术平台”建设思路，打通全矿山安全生产数据通道，实现企业生产信息化管理。
            </p>
          </div>
        </div>
      </div>
    </section>
    <!-- //content-6-section -->
    <!-- home page block grids -->
    <section class="w3l-text-11 py-5" id="blogs">
      <div class="container py-lg-5 py-md-4 py-2">
        <div class="header-section text-center mx-0 mb-md-5 mb-4">
          <h6 class="title-subhny">The core team</h6>
          <h3 class="title-w3l mt-2">核心团队</h3>
        </div>
        <div class="row text11-content">
          <div class="col-md-4 item mt-lg-0">
            <div class="card">
              <div class="card-header p-0 position-relative border-0">
                <a href="#">
                  <img
                    class="card-img-bottom d-block radius-image"
                    src="../assets/images/img4.jpg"
                    alt="Card image cap"
                  />
                </a>
              </div>
              <div class="card-body p-0 blog-details">
                <br />
                <a href="#" class="blog-desc"
                  >英国德蒙福特大学计算智能研究中心</a
                >
                <p>
                  Lorem ipsum, dolor sit amet consectetur adipisicing elit.
                  Vitae voluptatum.
                </p>
                <a
                  href="https://www.dmu.ac.uk/research/research-faculties-and-institutes/technology/cci/centre-for-computational-intelligence.aspx"
                  class="btn btn-style btn-primary mt-lg-4 mt-4"
                  >Read More
                  <span class="fa fa-arrow-right ml-2" aria-hidden="true"></span
                ></a>
              </div>
            </div>
          </div>

          <div class="col-md-4 item mt-lg-0 mt-5">
            <div class="card">
              <div class="card-header p-0 position-relative border-0">
                <a href="#">
                  <img
                    class="card-img-bottom d-block radius-image"
                    src="../assets/images/img5.jpg"
                    alt="Card image cap"
                  />
                </a>
              </div>
              <div class="card-body p-0 blog-details">
                <br />
                <a href="#" class="blog-desc"
                  >湘潭大学计算机学院·网络空间安全学院</a
                >
                <p>
                  Lorem ipsum, dolor sit amet consectetur adipisicing elit.
                  Vitae voluptatum.
                </p>
                <a
                  href="https://jwxy.xtu.edu.cn/"
                  class="btn btn-style btn-primary mt-lg-4 mt-4"
                  >Read More
                  <span class="fa fa-arrow-right ml-2" aria-hidden="true"></span
                ></a>
              </div>
            </div>
          </div>

          <div class="col-md-4 item mt-lg-0 mt-5">
            <div class="card">
              <div class="card-header p-0 position-relative border-0">
                <a href="#">
                  <img
                    class="card-img-bottom d-block radius-image"
                    src="../assets/images/img4.jpg"
                    alt="Card image cap"
                  />
                </a>
              </div>
              <div class="card-body p-0 blog-details">
                <br />
                <a href="#" class="blog-desc"
                  >中国地质大学（武汉）自动化学院·计算机学院</a
                >
                <p>
                  Lorem ipsum, dolor sit amet consectetur adipisicing elit.
                  Vitae voluptatum.
                </p>
                <a
                  href="https://au.cug.edu.cn/"
                  class="btn btn-style btn-primary mt-lg-4 mt-4"
                  >Read More
                  <span class="fa fa-arrow-right ml-2" aria-hidden="true"></span
                ></a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- //home page block grids -->
    <!-- stats -->

    <section class="w3l-stats py-5">
      <div class="container py-3">
        <div class="header-section text-center mx-0 mb-md-5 mb-4">
          <h6 class="title-subhny two">Our Stats</h6>
          <h3 class="title-w3l two mt-2">
            We believe in building long lasting <br />our business
            relationships.
          </h3>
        </div>
        <div class="row img-w3-content no-gutters">
          <div class="col-lg-6 img-right p-lg-0">
            <img
              src="../assets/images/img9.jpg"
              alt=""
              class="radius-image img-fluid"
            />
          </div>
          <div class="col-lg-6 stats-left">
            <div class="row stats-con">
              <div class="col-4 stats_info counter_grid">
                <p class="counter">1500</p>
                <h4>Projects</h4>
              </div>
              <div class="col-4 stats_info counter_grid">
                <p class="counter">1160</p>
                <h4>Employees</h4>
              </div>
              <div class="col-4 stats_info counter_grid2">
                <p class="counter">1145</p>
                <h4>Clients</h4>
              </div>
              <p class="mt-2 mb-3">
                Lorem ipsum viverra feugiat. Pellen tesque libero ut justo,
                ultrices in ligula. Semper at tempufddfel.Lorem ipsum, dolor sit
                amet consectetur adipisicing elit. Vitae voluptatum.Semper at
                tempufddfe.
              </p>
              <a class="btn btn-style btn-primary mt-4" href="about.html"
                >Read More
                <span class="fa fa-arrow-right ml-2" aria-hidden="true"></span
              ></a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- //stats-->
    <!-- testimonials section -->
    <section class="w3l-clients w3l-test pb-5" id="testimonials">
      <div class="midd-w3 py-5">
        <div class="container py-lg-5 py-md-4 pt-2 pb-lg-5">
          <div
            class="header-section text-center mx-0 mb-md-5 mb-4 pt-lg-5 pt-4"
          >
            <h6 class="title-subhny">Happy Clients</h6>
            <h3 class="title-w3l mt-2">What Our Clients Say</h3>
          </div>
          <div
            id="owl-demo2"
            class="owl-carousel owl-theme mt-4 py-md-2 mb-md-4"
          >
            <div class="item">
              <div class="testimonial-content">
                <div class="testimonial">
                  <blockquote>
                    <q>Pellen tesque libero ut justo</q>
                  </blockquote>
                  <p>
                    Lorem ipsum dolor sit amet elit. hic odio tenetur. ante
                    ipsum primis in faucibus orci luctus.
                  </p>
                </div>
                <div class="bottom-info mt-4">
                  <a class="comment-img" href="#url"
                    ><img
                      src="../assets/images/team1.jpg"
                      class="img-responsive"
                      alt="placeholder image"
                  /></a>
                  <div class="people-info align-self">
                    <h3>Johnson william</h3>
                    <p class="identity">Example City</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="item">
              <div class="testimonial-content">
                <div class="testimonial">
                  <blockquote>
                    <q>Lorem ipsum dolor sit amet</q>
                  </blockquote>
                  <p>
                    Lorem ipsum dolor sit amet elit. hic odio tenetur. ante
                    ipsum primis in faucibus orci luctus.
                  </p>
                </div>
                <div class="bottom-info mt-4">
                  <a class="comment-img" href="#url"
                    ><img
                      src="../assets/images/team2.jpg"
                      class="img-responsive"
                      alt="placeholder image"
                  /></a>
                  <div class="people-info align-self">
                    <h3>Alexander sakura</h3>
                    <p class="identity">Example City</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="item">
              <div class="testimonial-content">
                <div class="testimonial">
                  <blockquote>
                    <q>Pellen tesque libero ut justo</q>
                  </blockquote>
                  <p>
                    Lorem ipsum dolor sit amet elit. hic odio tenetur. ante
                    ipsum primis in faucibus orci luctus.
                  </p>
                </div>
                <div class="bottom-info mt-4">
                  <a class="comment-img" href="#url"
                    ><img
                      src="../assets/images/team3.jpg"
                      class="img-responsive"
                      alt="placeholder image"
                  /></a>
                  <div class="people-info align-self">
                    <h3>John wilson</h3>
                    <p class="identity">Example City</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="item">
              <div class="testimonial-content">
                <div class="testimonial">
                  <blockquote>
                    <q>Lorem ipsum dolor sit amet</q>
                  </blockquote>
                  <p>
                    Lorem ipsum dolor sit amet elit. hic odio tenetur. ante
                    ipsum primis in faucibus orci luctus.
                  </p>
                </div>
                <div class="bottom-info mt-4">
                  <a class="comment-img" href="#url"
                    ><img
                      src="../assets/images/team4.jpg"
                      class="img-responsive"
                      alt="placeholder image"
                  /></a>
                  <div class="people-info align-self">
                    <h3>Julia sakura</h3>
                    <p class="identity">Example City</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="item">
              <div class="testimonial-content">
                <div class="testimonial">
                  <blockquote>
                    <q>Pellen tesque libero ut justo</q>
                  </blockquote>
                  <p>
                    Lorem ipsum dolor sit amet elit. hic odio tenetur. ante
                    ipsum primis in faucibus orci luctus.
                  </p>
                </div>
                <div class="bottom-info mt-4">
                  <a class="comment-img" href="#url"
                    ><img
                      src="../assets/images/team5.jpg"
                      class="img-responsive"
                      alt="placeholder image"
                  /></a>
                  <div class="people-info align-self">
                    <h3>John wilson</h3>
                    <p class="identity">Example City</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="item">
              <div class="testimonial-content">
                <div class="testimonial">
                  <blockquote>
                    <q>Lorem ipsum dolor sit amet.</q>
                  </blockquote>
                  <p>
                    Lorem ipsum dolor sit amet elit. hic odio tenetur. ante
                    ipsum primis in faucibus orci luctus.
                  </p>
                </div>
                <div class="bottom-info mt-4">
                  <a class="comment-img" href="#url"
                    ><img
                      src="../assets/images/team3.jpg"
                      class="img-responsive"
                      alt="placeholder image"
                  /></a>
                  <div class="people-info align-self">
                    <h3>Julia sakura</h3>
                    <p class="identity">Example City</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- //testimonials section -->
    <!-- footer-28 block -->
    <footer class="footer-28 position-relative py-5">
      <div class="container py-lg-3">
        <div class="w3l-forms-9 px-md-2" id="newsletter">
          <div class="main-w3 py-4">
            <div class="container-fluid py-lg-3 py-2">
              <div class="row align-items-center">
                <div class="main-midd col-lg-6">
                  <h4 class="">Subscribe our newsletter</h4>
                  <p>We’re a team of non-cynics who truly care for our work.</p>
                </div>
                <div class="main-midd-2 col-lg-6 mt-lg-0 mt-4">
                  <form
                    action="#url"
                    method="GET"
                    class="rightside-form d-sm-flex"
                  >
                    <input
                      type="email"
                      class="form-control"
                      name="email"
                      placeholder="Enter your email"
                    />
                    <button class="btn" type="submit">Subscribe</button>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row footer-top-28 mt-4">
          <div class="col-lg-5 footer-list-28 pr-lg-5 mt-5">
            <h6 class="footer-title-28">Quick Contact</h6>
            <p class="pr-lg-5">
              Lorem ipsum viverra feugiat. Pellen tesque libero ut justo,
              ultrices in ligula. Semper at tempufddfel. Learn more about our
              work! Lorem ipsum viverra feugiat.
            </p>

            <div class="main-social-footer-28 mt-4">
              <ul class="social-icons">
                <li class="facebook">
                  <a href="#link" title="Facebook">
                    <span class="fa fa-facebook" aria-hidden="true"></span>
                  </a>
                </li>
                <li class="twitter">
                  <a href="#link" title="Twitter">
                    <span class="fa fa-twitter" aria-hidden="true"></span>
                  </a>
                </li>
                <li class="dribbble">
                  <a href="#link" title="Dribbble">
                    <span class="fa fa-dribbble" aria-hidden="true"></span>
                  </a>
                </li>
                <li class="google">
                  <a href="#link" title="Google">
                    <span class="fa fa-google" aria-hidden="true"></span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
          <div class="col-lg-7">
            <div class="row">
              <div class="col-md-3 col-sm-6 footer-list-28 mt-5">
                <h6 class="footer-title-28">Quick Links</h6>
                <ul>
                  <li>
                    <a href="index.html"
                      ><span
                        class="fa fa-arrow-right mr-2"
                        aria-hidden="true"
                      ></span>
                      Home</a
                    >
                  </li>
                  <li>
                    <a href="about.html"
                      ><span
                        class="fa fa-arrow-right mr-2"
                        aria-hidden="true"
                      ></span>
                      About us</a
                    >
                  </li>
                  <li>
                    <a href="services.html"
                      ><span
                        class="fa fa-arrow-right mr-2"
                        aria-hidden="true"
                      ></span>
                      Services</a
                    >
                  </li>
                  <li>
                    <a href="blog.html"
                      ><span
                        class="fa fa-arrow-right mr-2"
                        aria-hidden="true"
                      ></span>
                      Blog Posts</a
                    >
                  </li>
                  <li>
                    <a href="contact.html"
                      ><span
                        class="fa fa-arrow-right mr-2"
                        aria-hidden="true"
                      ></span>
                      Contact</a
                    >
                  </li>
                </ul>
              </div>
              <div class="col-md-5 col-sm-6 footer-list-28 mt-5">
                <h6 class="footer-title-28">Our Services</h6>
                <ul>
                  <li>
                    <a href="#reserch"
                      ><span
                        class="fa fa-arrow-right mr-2"
                        aria-hidden="true"
                      ></span>
                      Chemical Reserch</a
                    >
                  </li>
                  <li>
                    <a href="#construction"
                      ><span
                        class="fa fa-arrow-right mr-2"
                        aria-hidden="true"
                      ></span>
                      Construction Materials</a
                    >
                  </li>
                  <li>
                    <a href="#agricultural"
                      ><span
                        class="fa fa-arrow-right mr-2"
                        aria-hidden="true"
                      ></span>
                      Agricultural Engineering</a
                    >
                  </li>
                  <li>
                    <a href="#bridge"
                      ><span
                        class="fa fa-arrow-right mr-2"
                        aria-hidden="true"
                      ></span>
                      Bridge Engineering</a
                    >
                  </li>
                  <li>
                    <a href="#automotive"
                      ><span
                        class="fa fa-arrow-right mr-2"
                        aria-hidden="true"
                      ></span>
                      Automotive & System</a
                    >
                  </li>
                </ul>
              </div>
              <div class="col-md-4 col-sm-6 footer-list-28 mt-5">
                <h6 class="footer-title-28">Help</h6>
                <ul>
                  <li>
                    <a href="#privacy"
                      ><span
                        class="fa fa-arrow-right mr-2"
                        aria-hidden="true"
                      ></span>
                      Privacy policy</a
                    >
                  </li>
                  <li>
                    <a href="#support"
                      ><span
                        class="fa fa-arrow-right mr-2"
                        aria-hidden="true"
                      ></span>
                      Support</a
                    >
                  </li>
                  <li>
                    <a href="#terms"
                      ><span
                        class="fa fa-arrow-right mr-2"
                        aria-hidden="true"
                      ></span>
                      Terms & conditions</a
                    >
                  </li>
                  <li>
                    <a href="#license"
                      ><span
                        class="fa fa-arrow-right mr-2"
                        aria-hidden="true"
                      ></span>
                      License and uses</a
                    >
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div class="midd-footer-28 align-center py-4 mt-5">
          <p class="copy-footer-28 text-center">
            &copy; 2021 Sectoral. All Rights Reserved. Design by
            <!-- <a href="https://w3layouts.com/" target="_blank"> W3layouts</a> -->
          </p>
        </div>
      </div>

      <button onclick="topFunction()" id="movetop" title="Go to top">
        &#10548;
      </button>
    </footer>
  </div>
</template>

<script>
import "../assets/css/index.css";

export default {
  props: {},
  components: {},
  data() {
    return {};
  },
  methods: {
    topFunction: function () {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    },
    login: function () {
     this.$router.push('/login');
    },
  },
};
</script>

<style lang="less">
header {
  background-color: #8d490b;
  opacity: 0.8;
  margin-bottom: 20px;
}
#about {
  margin-top: 10px;
}
.intro {
  height: 100vh;
  background: url("../assets/images/bg.jpg") no-repeat fixed top center/ cover;
}

.intro-content > h1 {
  color: #fff;
  font-size: 40px;
  font-weight: 900;
  margin-bottom: 25px;
  text-transform: uppercase;
  text-shadow: 0px 0px 20px #000;
}

.intro-content > a > i.lnr {
  font-size: 10px;
  margin-left: 5px;
}

.intro-content > p {
  color: #f8f8f8;
  font-size: 15px;
  text-shadow: 0px 0px 20px #000;
  /* font-style: italic; */
  line-height: 1.5;
  margin-bottom: 45px;
  max-width: 450px;
}

.intro .carousel-indicators {
  bottom: 0;
  margin-bottom: -20%;
}

.intro .carousel-indicators li {
  background-color: #00bcd4;
  border: 2px solid #00bcd4;
  height: 15px;
  width: 15px;
  margin: 4px;
}

.intro .carousel-indicators .active {
  background-color: #fff;
  border: 3px solid #fff !important;
  height: 13px;
  margin: 5px;
  width: 13px;
}
.container {
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
}

@media (min-width: 768px) {
  .container {
    width: 750px;
  }
}

@media (min-width: 992px) {
  .container {
    width: 970px;
  }
}

@media (min-width: 1200px) {
  .container {
    width: 1170px;
  }
}

.container-fluid {
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
}
.Title {
  margin-top: 40%;
  //   background-color: azure;
  opacity: 0.8;
}
.ti {
  width: 890px;
}
.loginButton {
  z-index: 1;
  position: relative;
  font-size: inherit;
  font-family: inherit;
  // color: white;
  padding: 0.5em 1em;
  outline: none;
  border: none;
  background-color: #714724;
  overflow: hidden;
  transition: color 0.4s ease-in-out;
}

.loginButton::before {
  content: "";
  z-index: -1;
  position: absolute;
  top: 50%;
  left: 50%;
  width: 1em;
  height: 1em;
  border-radius: 50%;
  background-color: #ccd7e5;
  transform-origin: center;
  transform: translate3d(-50%, -50%, 0) scale3d(0, 0, 0);
  transition: transform 0.45s ease-in-out;
}

.loginButtonton:hover {
  cursor: pointer;
  color: #161616;
}

.loginButton:hover::before {
  transform: translate3d(-50%, -50%, 0) scale3d(15, 15, 15);
}
</style>