# SmartMine







## Project name

smartmine

## System architecture

![](https://cdn.jsdelivr.net/gh/wkif/ImageHosting@master/kif_img/20211026122820.png)



## Development technology selection

### Development mode

Front end and back end separated



### Front End Frame

Vue.js v2.5.2  (https://cn.vuejs.org/)

### UI framework

Ant Design Vue  v1.7.8 (https://www.antdv.com/)



### The back-end framework

django V3.2.6 (https://www.djangoproject.com/)



### The database

Mysql v5.7.26 (https://www.mysql.com/)



## Project planning

```mermaid
gantt
title  智慧矿山管理系统项目规划

dateFormat YYYY-MM-DD

section 设备管理

数据库设计:done,des1,2021-08-21,10d
前端UI设计:done,des1,2021-08-21,10d
接口设计:done,des2,after des1,6d
后端接口编写:done,des3,after des2,14d
api接口测试:done,des4,after des3,5d
前端编写:done,des5,after des2,14d
测试:done,des6,after des5,5d

section 人力资源管理
架构设计:done,des7,2021-09-25,4d
数据库设计:done,des7,2021-09-25,4d
前端UI设计:done,des8,2021-09-11,7d
架构设计:done,des9,after des7,3d
后端接口编写:crit,active,des10,after des9,20d
api接口测试:des11,after des10,5d
前端编写:des12,after des9,28d
测试 :des13,after des12,5d

section 安全管理
架构设计:done,des14,2021-08-21,10d
数据库设计:done,des14,2021-08-21,10d
接口设计:done,des15,after des14,6d
后端接口编写:done,des16,after des15,14d
api接口测试:done,des17,after des16,5d
前端编写:des18,after des13,10d
测试:des19,after des18,4d

section 生产管理

结构设计:des20,after des19,10d
数据库设计:des20,after des19,10d
接口设计:des21,after des20,6d
后端接口编写:des22,after des21,14d
api接口测试:des23,after des22,5d
前端编写:des24,after des21,19d

```





## Project directory



```

├── README.md
├── smartminefrontend
│   ├── build
│   │   ├── build.js
│   │   ├── check-versions.js
│   │   ├── logo.png
│   │   ├── utils.js
│   │   ├── vue-loader.conf.js
│   │   ├── webpack.base.conf.js
│   │   ├── webpack.dev.conf.js
│   │   └── webpack.prod.conf.js
│   ├── config
│   │   ├── dev.env.js
│   │   ├── index.js
│   │   └── prod.env.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
│   ├── src
│   │   ├── App.vue
│   │   ├── assets
│   │   ├── components
│   │   ├── main.js
│   │   └── router
│   └── static
├── smartmine_django
│   ├── api
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── extensions
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── utils
│   │   ├── views.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── db.sqlite3
│   ├── manage.py
│   ├── media
│   ├── requirements.txt
│   ├── smartmine_django
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── static
│   │   └── demoUploduser.xlsx
│   └── venv
│       ├── Lib
│       ├── pyvenv.cfg
│       └── Scripts

```

