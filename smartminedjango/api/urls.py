from django.urls import path, include
from api import views

urlpatterns = [

    # 2表示已经完成接口编写，1表示前端已经在使用

    # 人力资源管理------------------start---------------------------
    path('register/', views.registerApi.as_view()),
    # 12
    path('login/', views.loginApi.as_view()),
    # 12
    path('getalluser/', views.getalluser.as_view()),
    # 12
    path('deleteuser/', views.deleteuser.as_view()),
    # 12
    path('getuserinfo/', views.getuserinfo.as_view()),
    # 12
    path('add_user/', views.add_user.as_view()),
    # 12
    path('edituserinfo/', views.edituserinfo.as_view()),
    # 12
    path('edituserinfoBYadmin/', views.edituserinfoBYadmin.as_view()),
    # 12
    path('changepassword/', views.changepassword.as_view()),
    # 12
    path('changeEmail/', views.changeEmail.as_view()),
    # 12
    path('getemailcode/', views.getemailcode.as_view()),
    # 12
    path('downloadxlsxdemo/', views.downloadxlsxdemo.as_view()),
    # 12

    # path('add_organization_structure/', views.add_organization_structure.as_view()),
    # path('delete_organization_structure/', views.delete_organization_structure.as_view()),
    # path('change_organization_structure/', views.change_organization_structure.as_view()),
    # path('get_organization_structure/', views.get_organization_structure.as_view()),

    # 人力资源管理------------------end---------------------------

    # 设备管理-----------------------start----------------------------------

    path('add_device_type/', views.add_device_type.as_view(), name='增加设备类型'),
    # 12
    path('get_device_type_Data/', views.get_device_type_Data.as_view(), name='获取设备类型数据'),
    # 12
    path('get_all_device/', views.get_all_device.as_view(), name='获取所有设备信息'),
    # 12
    path('add_one_device/', views.add_one_device.as_view(), name='增加具体设备'),
    # 12
    path('delete_one_device/', views.delete_one_device.as_view(), name='删除具体设备'),
    #
    path('add_person_to_device/', views.add_person_to_device.as_view(), name='增加人员与使用设备'),
    # 12

    path('start_device/', views.start_device.as_view(), name='开始运行设备'),
    # 2
    path('end_device/', views.end_device.as_view(), name='结束运行设备'),
    # 2

    path('add_monitor_type/', views.add_monitor_type.as_view(), name='增加设备监控值类型'),
    # 2
    path('error_upload/', views.error_upload.as_view(), name='设备异常上报'),
    # 2
    # 设备管理-----------------------end----------------------------------
    # 安全管理-----------------------start----------------------------------
    path('add_env_warn_type/', views.add_env_warn_type.as_view(), name='增加环境预警类型'),
    # 2
    path('delete_env_warn_type/', views.delete_env_warn_type.as_view(), name='删除环境预警类型'),
    # 2
    path('change_env_warn_type/', views.change_env_warn_type.as_view(), name='修改环境预警类型'),
    # 2
    path('get_env_warn_type/', views.get_env_warn_type.as_view(), name='删除环境预警类型'),
    # 2
    path('add_env_exception/', views.add_env_exception.as_view(), name='环境预警上报'),
    # 2
    path('get_env_exception/', views.get_env_exception.as_view(), name='查看环境预警记录'),
    # 2

    path('add_person_illegel_type/', views.add_person_illegel_type.as_view(), name='增加人员违规操作类型'),
    # 2
    path('delete_person_illegel_type/', views.delete_person_illegel_type.as_view(), name='删除人员违规操作类型'),
    # 2
    path('get_person_illegel_type/', views.get_person_illegel_type.as_view(), name='删除人员违规操作类型'),
    # 2
    path('add_person_illegel_upload/', views.add_person_illegel_upload.as_view(), name='人员违规操作上报'),
    # 2
    path('get_person_illegel_upload/', views.get_person_illegel_upload.as_view(), name='人员违规操作上报记录'),
    # 2
    path('delete_person_illegel_upload/', views.delete_person_illegel_upload.as_view(), name='删除人员违规操作上报记录'),
    # 2
    # 安全管理-----------------------end----------------------------------
]
