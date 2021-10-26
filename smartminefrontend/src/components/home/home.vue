<template>
  <div>
    <a-row>
      <a-col :span="6">
        <a-card>
          <p>地层温度监测</p>
          <div style="background-color: #ececec">
            <div style="width: auto; height: 400px" id="Heat_map"></div>
          </div>
        </a-card>
        <a-card>
          <div style="width: 100%">
            <a-radio-group v-model="Classification_of_dimensions">
              <a-radio-button value="day"> 日 </a-radio-button>
              <a-radio-button value="mouth"> 月 </a-radio-button>
              <a-radio-button value="year"> 年 </a-radio-button>
            </a-radio-group>
          </div>
          <div style="background-color: #ececec">
            <a-row :gutter="16">
              <a-col :span="12">
                <a-card title="报警总数" :bordered="false">
                  <p>12</p>
                </a-card>
              </a-col>
              <a-col :span="12">
                <a-card title="未处理报警" :bordered="false">
                  <p>12</p>
                </a-card>
              </a-col>
            </a-row>
          </div>
          <p>报警类型统计</p>
          <div style="background-color: #ececec">
            <div style="width: auto; height: 400px" id="Alarm_type"></div>
          </div>
          <p>报警等级统计</p>
          <div style="background-color: #ececec">
            <div style="width: auto; height: 400px" id="Alarm_level"></div>
          </div>
        </a-card>
      </a-col>
      <a-col :span="12">
        <div style="background-color: #ececec">
          <div style="width: auto; height: 900px" id="map"></div>
        </div>
        <a-card>
          <p></p>
          <div style="background-color: #ececec">
            <div style="width: auto; height: 600px" id="traffic"></div>
          </div>
        </a-card>
      </a-col>
      <a-col :span="6">
        <a-card>
          <p>司机违规列表</p>
          <div style="background-color: #ececec">
            <div
              style="width: auto; height: 400px"
              id="Driver_violation_list"
            ></div>
          </div>
        </a-card>
        <a-card>
          <p>作业人员统计</p>
          <div style="background-color: #ececec">
            <div
              style="width: auto; height: 400px"
              id="Operator_statistics"
            ></div>
          </div>
        </a-card>
        <a-card>
          <p>设备状态</p>
          <div style="background-color: #ececec">
            <div style="width: auto; height: 540px" id="Equipment_state"></div>
          </div>
        </a-card>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import * as echarts from "echarts";
import "echarts-gl";

export default {
  props: {},
  components: {},
  data() {
    return {
      weatherData: {
        area: "米拉多",
        temperature: 26,
        rainfall: "100mm",
        windSpeed: "60m/s",
      },
      Classification_of_dimensions: "",
    };
  },
  mounted() {
    this.Heat_map();
    this.map();
    this.Alarm_type();
    this.Alarm_level();
    this.Driver_violation_list();
    this.Operator_statistics();
    this.Equipment_state();
    this.traffic();
  },

  methods: {
    Heat_map() {
      var chartDom_Heat_map = document.getElementById("Heat_map");
      var myChart_Heat_map = echarts.init(chartDom_Heat_map, "dark");
      var option;

      $.getScript(
        "https://cdn.jsdelivr.net/npm/simplex-noise@2.4.0/simplex-noise.js"
      ).done(function () {
        var noise = new SimplexNoise(Math.random);
        function generateData(theta, min, max) {
          var data = [];
          for (var i = 0; i <= 20; i++) {
            for (var j = 0; j <= 20; j++) {
              for (var k = 0; k <= 20; k++) {
                var value = noise.noise3D(i / 10, j / 10, k / 10);
                valMax = Math.max(valMax, value);
                valMin = Math.min(valMin, value);
                data.push([i, j, k, value * 2 + 4]);
              }
            }
          }
          return data;
        }
        var valMin = Infinity;
        var valMax = -Infinity;
        var data = generateData(2, -5, 5);

        myChart_Heat_map.setOption(
          (option = {
            visualMap: {
              show: false,
              min: 2,
              max: 6,
              inRange: {
                symbolSize: [0.5, 25],
                color: [
                  "#313695",
                  "#4575b4",
                  "#74add1",
                  "#abd9e9",
                  "#e0f3f8",
                  "#ffffbf",
                  "#fee090",
                  "#fdae61",
                  "#f46d43",
                  "#d73027",
                  "#a50026",
                ],
                colorAlpha: [0.2, 1],
              },
            },
            xAxis3D: {
              type: "value",
            },
            yAxis3D: {
              type: "value",
            },
            zAxis3D: {
              type: "value",
            },
            grid3D: {
              axisLine: {
                lineStyle: { color: "#fff" },
              },
              axisPointer: {
                lineStyle: { color: "#fff" },
              },
              viewControl: {
                // autoRotate: true
              },
            },
            series: [
              {
                type: "scatter3D",
                data: data,
              },
            ],
          })
        );
      });

      option && myChart_Heat_map.setOption(option);
    },
    map() {
      var ROOT_PATH =
        "https://cdn.jsdelivr.net/gh/apache/echarts-website@asf-site/examples";
      var chartDom_map = document.getElementById("map");
      var myChart_map = echarts.init(chartDom_map);
      var option_map;
      $.getJSON(
        ROOT_PATH + "/data-gl/asset/data/buildings.json",
        function (buildingsGeoJSON) {
          echarts.registerMap("buildings", buildingsGeoJSON);

          var regions = buildingsGeoJSON.features.map(function (feature) {
            return {
              name: feature.properties.name,
              value: Math.max(Math.sqrt(feature.properties.height), 0.1),
              height: Math.max(Math.sqrt(feature.properties.height), 0.1),
            };
          });

          myChart_map.setOption({
            series: [
              {
                type: "map3D",
                map: "buildings",
                shading: "realistic",
                realisticMaterial: {
                  roughness: 0.6,
                  textureTiling: 20,
                  detailTexture: ROOT_PATH + "/data-gl/asset/woods.jpg",
                },
                postEffect: {
                  enable: true,
                  bloom: {
                    enable: false,
                  },
                  SSAO: {
                    enable: true,
                    quality: "medium",
                    radius: 10,
                    intensity: 1.2,
                  },
                  depthOfField: {
                    enable: false,
                    focalRange: 5,
                    fstop: 1,
                    blurRadius: 6,
                  },
                },
                groundPlane: {
                  show: true,
                  color: "#333",
                },
                light: {
                  main: {
                    intensity: 6,
                    shadow: true,
                    shadowQuality: "high",
                    alpha: 30,
                  },
                  ambient: {
                    intensity: 0,
                  },
                  ambientCubemap: {
                    texture: ROOT_PATH + "/data-gl/asset/canyon.hdr",
                    exposure: 2,
                    diffuseIntensity: 1,
                    specularIntensity: 1,
                  },
                },
                viewControl: {
                  minBeta: -360,
                  maxBeta: 360,
                },
                itemStyle: {
                  areaColor: "#666",
                },
                label: {
                  color: "white",
                },
                silent: true,
                instancing: true,
                boxWidth: 200,
                boxHeight: 1,
                data: regions,
              },
            ],
          });
        }
      );
      option_map && myChart_map.setOption(option_map);
    },
    Alarm_type() {
      var chartDom_Alarm_type = document.getElementById("Alarm_type");
      var myChart_Alarm_type = echarts.init(chartDom_Alarm_type);
      var option;

      option = {
        xAxis: {
          type: "category",
          data: ["司机疲劳驾驶", "未佩戴安全帽", "障碍预警", "底油位", "低压"],
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            data: [9, 7, 5, 2, 2],
            type: "bar",
            showBackground: true,
            backgroundStyle: {
              color: "rgba(180, 180, 180, 0.2)",
            },
          },
        ],
      };

      option && myChart_Alarm_type.setOption(option);
    },
    Alarm_level() {
      var chartDom_Alarm_level = document.getElementById("Alarm_level");
      var myChart_Alarm_level = echarts.init(chartDom_Alarm_level);
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
            name: "报警等级统计",
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
            data: [
              { value: 12, name: "一级" },
              { value: 9, name: "二级" },
              { value: 2, name: "三级" },
            ],
          },
        ],
      };

      option && myChart_Alarm_level.setOption(option);
    },
    Equipment_state() {
      var chartDom_Equipment_state = document.getElementById("Equipment_state");
      var myChart_Equipment_state = echarts.init(chartDom_Equipment_state);
      var option;

      option = {
        title: {
          text: "设备状态",
          // subtext: "From ExcelHome",
          sublink: "http://e.weibo.com/1341556070/Aj1J2x5a5",
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: "shadow", // 默认为直线，可选为：'line' | 'shadow'
          },
          formatter: function (params) {
            var tar;
            if (params[1].value !== "-") {
              tar = params[1];
            } else {
              tar = params[0];
            }
            return tar.name + "<br/>" + tar.seriesName + " : " + tar.value;
          },
        },
        legend: {
          data: ["工作", "休息"],
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: {
          type: "category",
          splitLine: { show: false },
          data: (function () {
            var list = [];
            for (var i = 1; i <= 11; i++) {
              list.push("设备" + i + "号");
            }
            return list;
          })(),
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            name: "辅助",
            type: "bar",
            stack: "总量",
            itemStyle: {
              barBorderColor: "rgba(0,0,0,0)",
              color: "rgba(0,0,0,0)",
            },
            emphasis: {
              itemStyle: {
                barBorderColor: "rgba(0,0,0,0)",
                color: "rgba(0,0,0,0)",
              },
            },
            data: [
              0, 900, 1245, 1530, 1376, 1376, 1511, 1689, 1856, 1495, 1292,
            ],
          },
          {
            name: "工作",
            type: "bar",
            stack: "总量",
            label: {
              show: true,
              position: "top",
            },
            data: [900, 345, 393, "-", "-", 135, 178, 286, "-", "-", "-"],
          },
          {
            name: "休息",
            type: "bar",
            stack: "总量",
            label: {
              show: true,
              position: "bottom",
            },
            data: ["-", "-", "-", 108, 154, "-", "-", "-", 119, 361, 203],
          },
        ],
      };

      option && myChart_Equipment_state.setOption(option);
    },
    Driver_violation_list() {
      var chartDom_Driver_violation_list = document.getElementById(
        "Driver_violation_list"
      );
      var myChart_Driver_violation_list = echarts.init(
        chartDom_Driver_violation_list
      );
      var option;

      option = {
        dataset: {
          source: [
            ["score", "amount", "product"],
            [89.3, 12, "Matcha Latte"],
            [57.1, 4, "Milk Tea"],
            [74.4, 12, "Cheese Cocoa"],
            [50.1, 13, "Cheese Brownie"],
            [89.7, 14, "Matcha Cocoa"],
            [68.1, 1, "Tea"],
            [19.6, 21, "Orange Juice"],
            [10.6, 4, "Lemon Juice"],
            [32.7, 11, "Walnut Brownie"],
          ],
        },
        grid: { containLabel: true },
        xAxis: { name: "amount" },
        yAxis: { type: "category" },
        visualMap: {
          orient: "horizontal",
          left: "center",
          min: 10,
          max: 100,
          text: ["High Score", "Low Score"],
          // Map the score column to color
          dimension: 0,
          inRange: {
            color: ["#65B581", "#FFCE34", "#FD665F"],
          },
        },
        series: [
          {
            type: "bar",
            encode: {
              // Map the "amount" column to X axis.
              x: "amount",
              // Map the "product" column to Y axis
              y: "product",
            },
          },
        ],
      };
      option && myChart_Driver_violation_list.setOption(option);
    },
    Operator_statistics() {
      var chartDom_Operator_statistics = document.getElementById(
        "Operator_statistics"
      );
      var myChart_Operator_statistics = echarts.init(
        chartDom_Operator_statistics
      );
      var option;

      option = {
        // title: {
        //   text: "作业人员统计",
        //   subtext: "数据来自网络",
        // },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },
        legend: {
          data: ["作业人员", "离岗人员"],
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: {
          type: "value",
          boundaryGap: [0, 0.01],
        },
        yAxis: {
          type: "category",
          data: ["A区", "B区", "C区", "D区", "E区", "F区"],
        },
        series: [
          {
            name: "作业人员",
            type: "bar",
            data: [12, 53, 54, 14, 86, 23],
          },
          {
            name: "离岗人员",
            type: "bar",
            data: [14, 9, 21, 21, 6, 14],
          },
        ],
      };

      option && myChart_Operator_statistics.setOption(option);
    },
    traffic() {
      var ROOT_PATH =
        "https://cdn.jsdelivr.net/gh/apache/echarts-website@asf-site/examples";

      var chartDom_traffic = document.getElementById("traffic");
      var myChart_traffic = echarts.init(chartDom_traffic);
      var option;

      $.get(
        ROOT_PATH + "/data/asset/geo/ksia-ext-plan-min.svg",
        function (svg) {
          echarts.registerMap("ksia-ext-plan", { svg: svg });

          option = {
            tooltip: {},
            geo: {
              map: "ksia-ext-plan",
              roam: true,
              layoutCenter: ["50%", "50%"],
              layoutSize: "100%",
            },
            series: [
              {
                name: "Route",
                type: "lines",
                coordinateSystem: "geo",
                geoIndex: 0,
                emphasis: {
                  label: {
                    show: false,
                  },
                },
                polyline: true,
                lineStyle: {
                  color: "#c46e54",
                  width: 0,
                },
                effect: {
                  show: true,
                  period: 8,
                  color: "#a10000",
                  // constantSpeed: 80,
                  trailLength: 0,
                  symbolSize: [12, 30],
                  symbol:
                    "path://M87.1667 3.8333L80.5.5h-60l-6.6667 3.3333L.5 70.5v130l10 10h80l10 -10v-130zM15.5 190.5l15 -20h40l15 20zm75 -65l-15 5v35l15 15zm-80 0l15 5v35l-15 15zm65 0l15 -5v-40l-15 20zm-50 0l-15 -5v-40l15 20zm 65,-55 -15,25 c -15,-5 -35,-5 -50,0 l -15,-25 c 25,-15 55,-15 80,0 z",
                },
                z: 100,
                data: [
                  {
                    effect: {
                      color: "#a10000",
                      constantSpeed: 100,
                      delay: 0,
                    },
                    coords: [
                      [50.875133928571415, 242.66287667410717],
                      [62.03696428571425, 264.482421875],
                      [72.63357421874997, 273.62779017857144],
                      [92.78291852678569, 285.869140625],
                      [113.43637834821425, 287.21854073660717],
                      [141.44788783482142, 288.92947823660717],
                      [191.71686104910714, 289.5507114955357],
                      [198.3060072544643, 294.0673828125],
                      [204.99699497767858, 304.60288783482144],
                      [210.79177734375003, 316.7373046875],
                      [212.45179408482142, 329.3656529017857],
                      [210.8885267857143, 443.3925083705358],
                      [215.35936941964286, 453.00634765625],
                      [224.38761997767858, 452.15087890625],
                      [265.71490792410714, 452.20179966517856],
                      [493.3408844866072, 453.77525111607144],
                      [572.8892940848216, 448.77992466517856],
                      [608.9513755580358, 448.43366350446433],
                      [619.99099609375, 450.8778599330358],
                      [624.2479715401787, 456.2194475446429],
                      [628.1434095982145, 463.9899553571429],
                      [629.8492550223216, 476.0276227678571],
                      [631.2750362723216, 535.7322126116071],
                      [624.6757059151787, 546.6496233258929],
                      [617.1801702008929, 552.6480887276786],
                      [603.7269056919645, 554.5066964285714],
                      [588.0178515625, 557.5517578125],
                      [529.4386104910716, 556.2991071428571],
                      [422.1994921875001, 551.38525390625],
                      [291.66921875, 552.5767996651786],
                      [219.4279380580357, 547.4949079241071],
                      [209.53912667410714, 541.5931919642858],
                      [206.70793247767858, 526.1947544642858],
                      [206.70793247767858, 507.4049944196429],
                      [206.12234375000003, 468.7663225446429],
                      [204.48778738839286, 459.44782366071433],
                      [197.56256417410714, 452.8943219866071],
                      [170.31995814732142, 456.27546037946433],
                      [1.8078906249999704, 460.5935407366071],
                    ],
                  },
                  {
                    effect: {
                      color: "#00067d",
                      constantSpeed: 80,
                      delay: 0,
                    },
                    coords: [
                      [779.4595368303574, 287.98744419642856],
                      [689.07009765625, 291.0477818080357],
                      [301.83300223214286, 290.49783761160717],
                      [229.31165736607142, 291.73011997767856],
                      [220.73660156250003, 297.4077845982143],
                      [214.74832031250003, 308.52378627232144],
                      [213.82156250000003, 421.35400390625],
                      [213.19523716517858, 443.0564313616071],
                      [222.31005301339286, 455.95465959821433],
                      [271.71846540178575, 454.37611607142856],
                      [359.64843191964286, 455.9393833705358],
                      [580.2524358258929, 448.11286272321433],
                      [627.7156752232145, 460.7463030133929],
                      [632.3290959821429, 536.6386021205358],
                      [628.9123130580358, 548.4776785714286],
                      [612.5667494419645, 556.8235909598214],
                      [543.7167912946429, 555.4741908482143],
                      [429.1756361607143, 551.9402901785714],
                      [293.42089285714286, 551.2172154017858],
                      [226.20039899553575, 556.0699637276786],
                      [215.49176339285714, 562.7253069196429],
                      [213.21051339285714, 591.6024693080358],
                      [212.00878348214286, 625.6735491071429],
                      [197.43017020089286, 645.0743582589286],
                      [187.41405691964286, 647.0857282366071],
                      [101.79589285714286, 649.0207170758929],
                      [69.96023437499997, 650.1613420758929],
                      [56.48150948660714, 656.8268694196429],
                      [51.11446149553569, 665.2542550223214],
                    ],
                  },
                  {
                    effect: {
                      color: "#997405",
                      constantSpeed: 60,
                      delay: 0,
                    },
                    coords: [
                      [2.5920703124999704, 450.66908482142856],
                      [204.0651450892857, 453.13364955357144],
                      [378.72844029017864, 453.13874162946433],
                      [551.1817745535716, 456.1532505580358],
                      [578.3734598214287, 456.91196986607144],
                      [601.2317885044645, 458.9895368303571],
                      [614.1503850446429, 462.1669921875],
                      [618.99294921875, 479.68882533482144],
                      [620.0826534598216, 513.5969587053571],
                      [615.6932840401787, 528.7306082589286],
                      [608.4829045758929, 533.2625558035714],
                      [592.7127455357145, 534.9582170758929],
                      [583.09890625, 527.5492466517858],
                      [578.6535239955358, 516.4077845982143],
                      [578.6535239955358, 498.36146763392856],
                      [577.9966462053571, 477.0613141741071],
                      [575.3691350446429, 469.1940569196429],
                      [569.0753292410716, 462.63037109375],
                      [553.9518638392858, 460.6444614955358],
                      [298.10051060267864, 465.61432756696433],
                      [193.49908761160714, 460.1759905133929],
                      [116.40505859374997, 465.78236607142856],
                      [3.5137360491071092, 463.47565569196433],
                    ],
                  },
                ],
              },
            ],
          };

          myChart_traffic.setOption(option);
        }
      );

      option && myChart_traffic.setOption(option);
    },
  },
};
</script>

<style lang="less" scoped>
.ant-card {
  margin: 10px;
}
</style>