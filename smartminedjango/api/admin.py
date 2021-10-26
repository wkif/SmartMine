from django.contrib import admin

admin.site.site_header = '智慧矿山管理后台'  # 设置header
admin.site.site_title = '智慧矿山管理后台'  # 设置title
admin.site.index_title = '智慧矿山管理后台'
# Register your models here.
from api.models import *


class userAdmin(admin.ModelAdmin):
    list_per_page = 20  # 指定每页显示20条数据
    list_display = ['id', 'username', 'password', 'realname', 'age', 'is_active', 'gender'
        , 'phone', 'userEmail', 'user_type']
    actions_on_bottom = True  # 在列表底部也显示操作动作的下拉框。 (默认只在列表顶部显示)
    actions_on_top = False  # 在列表顶部不显示操作动作的下拉框。
    list_filter = ['is_active', 'user_type' ]  # 列表页右侧过滤栏
    search_fields = ['id', 'username', 'realname']  # 列表页上方的搜索框


class specific_deviceAdmin(admin.ModelAdmin):
    list_per_page = 20  # 指定每页显示20条数据
    list_display = ['id', 'type', 'status', 'Equipment_serial_number', 'Running_state', 'is_active']
    actions_on_bottom = True  # 在列表底部也显示操作动作的下拉框。 (默认只在列表顶部显示)
    actions_on_top = False  # 在列表顶部不显示操作动作的下拉框。
    list_filter = ['is_active', 'status', 'Running_state']  # 列表页右侧过滤栏
    search_fields = ['id', 'type', 'Equipment_serial_number']  # 列表页上方的搜索框


class person2deviceAdmin(admin.ModelAdmin):
    list_per_page = 20  # 指定每页显示20条数据
    list_display = ['id', 'person', 'device_type']
    actions_on_bottom = True  # 在列表底部也显示操作动作的下拉框。 (默认只在列表顶部显示)
    actions_on_top = False  # 在列表顶部不显示操作动作的下拉框。
    search_fields = ['id', 'person', 'device_type']  # 列表页上方的搜索框

class device_typeAdmin(admin.ModelAdmin):
    list_per_page = 20  # 指定每页显示20条数据
    list_display = ['id', 'name', 'brief','value']
    actions_on_bottom = True  # 在列表底部也显示操作动作的下拉框。 (默认只在列表顶部显示)
    actions_on_top = False  # 在列表顶部不显示操作动作的下拉框。
    search_fields = ['id', 'name']  # 列表页上方的搜索框

class device_runningAdmin(admin.ModelAdmin):
    list_per_page = 20  # 指定每页显示20条数据
    list_display = ['id', 'person', 'device','start_time','end_time']
    actions_on_bottom = True  # 在列表底部也显示操作动作的下拉框。 (默认只在列表顶部显示)
    actions_on_top = False  # 在列表顶部不显示操作动作的下拉框。
    search_fields = ['id', 'person','device']  # 列表页上方的搜索框

class device_watch_typeAdmin(admin.ModelAdmin):
    list_per_page = 20  # 指定每页显示20条数据
    list_display = ['id', 'device_type', 'name','value_low','value_hign']
    actions_on_bottom = True  # 在列表底部也显示操作动作的下拉框。 (默认只在列表顶部显示)
    actions_on_top = False  # 在列表顶部不显示操作动作的下拉框。
    search_fields = ['id', 'device_type','name']  # 列表页上方的搜索框

class device_exceptionAdmin(admin.ModelAdmin):
    list_per_page = 20  # 指定每页显示20条数据
    list_display = ['id', 'upload_time', 'device', 'person', 'watch_value', 'watch']
    actions_on_bottom = True  # 在列表底部也显示操作动作的下拉框。 (默认只在列表顶部显示)
    actions_on_top = False  # 在列表顶部不显示操作动作的下拉框。
    list_filter = ['watch', 'device']  # 列表页右侧过滤栏
    search_fields = ['id', 'upload_time', 'device','person','watch']  # 列表页上方的搜索框

admin.site.register(user, userAdmin)
admin.site.register(specific_device, specific_deviceAdmin)
admin.site.register(person2device, person2deviceAdmin)
admin.site.register(device_type, device_typeAdmin)
admin.site.register(device_running, device_runningAdmin)
admin.site.register(device_watch_type, device_watch_typeAdmin)
admin.site.register(device_exception, device_exceptionAdmin)