import datetime
import os

from django.core.cache import cache
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from api.models import *
from api.serializers import userSerializer, specific_deviceSerializer, device_typeSerializer, env_warn_typeSerializer, \
    person_illegel_typeSerializer
from api.utils import email_send
from api.utils.createToken import creattoken
from api.extensions.auth import JwtQueryParamsAuthentication
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse

from smartmine_django.settings import STATICFILES_DIRS


# 人力资源管理------------------start---------------------------

class registerApi(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        res = {}
        u1 = user.objects.filter(username=username).first()
        u3 = user.objects.filter(userEmail=email).first()
        if u1:
            res['status'] = 400
            res['msg'] = "用户名已存在"
            return Response(res)
        elif u3:
            res['status'] = 400
            res['msg'] = "邮箱已经被注册"
            return Response(res)
        else:
            user.objects.create(username=username, userEmail=email, password=password)
            user.objects.update()
            res['status'] = 200
            res['msg'] = "注册成功"
            return Response(res)


class loginApi(APIView):
    def post(self, request):
        print(request.data.get)
        res = {}
        username = request.data.get('username')
        password = request.data.get('password')
        u1 = user.objects.filter(username=username).first()
        u2 = user.objects.filter(userEmail=username).first()
        print(u1)
        if u1:
            if password != u1.password:
                res['status'] = 400
                res['msg'] = "用户名或密码错误"
            else:
                token = creattoken(u1)
                re = userSerializer(u1)
                return JsonResponse({"info": re.data, "token": token, "status": 200})
        elif u2:
            if password != u2.password:
                res['status'] = 400
                res['msg'] = "用户名或密码错误"
            else:
                token = creattoken(u2)
                re = userSerializer(u2)
                return JsonResponse({"info": re.data, "token": token, "status": 200})
        else:
            res['status'] = 400
            res['msg'] = "用户名或密码错误"
        return Response(res)


class getalluser(APIView):
    # authentication_classes = [JwtQueryParamsAuthentication, ]

    def get(self, request):
        userData = user.objects.filter(is_active=True)
        re = userSerializer(userData, many=True)
        for x in re.data:
            devtypelist = []
            dev_id_List = person2device.objects.filter(person=user.objects.filter(id=x['id']).first())
            if dev_id_List:
                for dev in dev_id_List:
                    devtypelist.append(dev.device_type.name)
            x['device_type'] = devtypelist
        return Response({"info": re.data, "status": 200})


class deleteuser(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        id = request.data.get('id')
        us = user.objects.filter(id=id).first()
        if not us:
            return JsonResponse({"msg": "没有该用户", "status": 400})
        else:
            if not us.is_active:
                return JsonResponse({"msg": "没有该用户", "status": 400})
            else:
                us.is_active = False
                us.save()
                return JsonResponse({"msg": "删除成功", "status": 200})


class getuserinfo(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        id = request.data.get('id')
        u1 = user.objects.filter(id=id).first()
        if u1:
            re = userSerializer(u1)
            return JsonResponse({"info": re.data, "status": 200})
        else:
            return JsonResponse({"msg": "获取数据错误", "status": 400})


class add_user(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        realname = request.data.get('realname')
        phone = request.data.get('phone')
        gender = request.data.get('gender')
        user_type = request.data.get('user_type')
        u = user.objects.filter(phone=phone)
        if u:
            return JsonResponse({"msg": "手机号已经被注册", "status": 400})
        else:
            u = user.objects.create(username=phone, password=phone, realname=realname, gender=gender,
                                    phone=phone, user_type=user_type)
            res = {
                "errorcode": 0,
                "content": {
                    "msg": "保存成功",
                    "id": u.id
                }
            }
            return JsonResponse(res)


class edituserinfo(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        id = request.data.get('id')
        us = user.objects.filter(id=id).first()
        if not us:
            return JsonResponse({"msg": "没有该用户", "status": 400})
        else:
            if not us.is_active:
                return JsonResponse({"msg": "没有该用户", "status": 400})
            else:
                username = request.data.get('username')
                if user.objects.filter(username=username) and user.objects.filter(username=username).first().id != id:
                    return JsonResponse({"msg": "用户名已存在", "status": 400})
                else:
                    age = request.data.get('age')
                    gender = request.data.get('gender')
                    us.age = age
                    us.gender = gender
                    us.username = username
                    us.save()
                    re = userSerializer(us)
                    return JsonResponse({"msg": "修改成功", "info": re.data, "status": 200})


class edituserinfoBYadmin(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        id = request.data.get('id')
        us = user.objects.filter(id=id).first()
        if not us:
            return JsonResponse({"msg": "没有该用户", "status": 400})
        else:
            if not us.is_active:
                return JsonResponse({"msg": "没有该用户", "status": 400})
            else:
                realname = request.data.get('realname')
                phone = request.data.get('phone')
                age = request.data.get('age')
                userEmail = request.data.get('userEmail')
                gender = request.data.get('gender')
                user_type = request.data.get('user_type')
                department = request.data.get('department')
                us.realname = realname
                us.gender = gender
                us.phone = phone
                us.age = age
                us.userEmail = userEmail
                us.user_type = user_type
                us.department = department
                us.save()
                re = userSerializer(us)
                return JsonResponse({"msg": "修改成功", "info": re.data, "status": 200})


class changeusername(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        username = request.data.get('username')
        id = request.data.get('id')
        us = user.objects.filter(username=username)
        if us:
            return JsonResponse({"msg": "用户名已存在", "status": 400})
        else:
            theus = user.objects.filter(id=id).first()
            theus.username = username
            theus.save()
            return JsonResponse({"msg": "修改成功", "status": 200})


class changepassword(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        id = request.data.get('id')
        passwordLast = request.data.get('passwordLast')
        password = request.data.get('password')
        us = user.objects.filter(id=id).first()
        if us.password == passwordLast:
            us.password = password
            us.save()
            return JsonResponse({"msg": "修改成功", "status": 200})
        else:
            return JsonResponse({"msg": "原密码错误", "status": 400})


class changeEmail(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        email = request.data.get('email')
        code = email_send.send_code_email(email, "changeEmail")
        cache.set(email, code, 120)
        if code:
            return JsonResponse({"msg": "验证码已发送", "status": 200})


class getemailcode(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        id = request.data.get('id')
        email = request.data.get('email')
        code = request.data.get('code')
        res = cache.get(email)
        if not res:
            return JsonResponse({"msg": "验证码已过期", "status": 400})
        else:
            if code != res:
                return JsonResponse({"msg": "验证码错误", "status": 400})
            else:
                us = user.objects.filter(id=id).first()
                us.userEmail = email
                us.save()
                return JsonResponse({"msg": "已更改", "status": 200})


# 人力资源管理------------------end---------------------------


class get_all_device(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def get(self, request):
        deviceData = specific_device.objects.filter(is_active=True)
        data2 = [
            {'key': 0, 'value': 0, 'name': '正常'},
            {'key': 1, 'value': 0, 'name': '故障'},
            {'key': 2, 'value': 0, 'name': '维修中'},
        ]
        for dev in deviceData:
            if dev.status == "0":
                dev.status = "正常"
                data2[0]['value'] += 1
            elif dev.status == "1":
                dev.status = "故障"
                data2[1]['value'] += 1
            else:
                dev.status = "维修中"
                data2[2]['value'] += 1
            if dev.Running_state == "1":
                dev.Running_state = "运行中"
            else:
                dev.Running_state = "休息"
            # tyid = dev.type.id
            # dev.type=device_type.objects.filter(id=tyid).first().name
        re = specific_deviceSerializer(deviceData, many=True)
        return Response({"info": re.data, "info2": data2, "status": 200})


class add_device_type(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        name = request.data.get('name')
        de = device_type.objects.filter(name=name)
        if de:
            return JsonResponse({"msg": "此种设备已存在", "status": 400})
        else:
            de = device_type.objects.create(name=name)
            res = {
                "errorcode": 0,
                "content": {
                    "id": de.id
                }
            }
            return JsonResponse(res)


class get_device_type_Data(APIView):
    # authentication_classes = [JwtQueryParamsAuthentication, ]

    def get(self, request):
        dev_ty = device_type.objects.all()
        # tyname=[]
        # tynumber=[]
        # for ty in dev_ty:
        #     tyname.append(ty.name)
        #     tynumber.append(ty.number)
        # data={}
        # data['tyname']=tyname
        # data['tynumber']=tynumber
        # return Response({"data": data, "status": 200})
        re1 = device_typeSerializer(dev_ty, many=True)

        return Response({"info": re1.data, "status": 200})


class add_one_device(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        device_type_name = request.data.get('device_type_name')
        Equipment_serial_number = request.data.get('Equipment_serial_number')
        device_ty = device_type.objects.filter(name=device_type_name).first()
        if not device_ty:
            device_type.objects.create(name=device_type_name)
        device_ty = device_type.objects.filter(name=device_type_name).first()
        d = specific_device.objects.create(type=device_ty, status=0, Equipment_serial_number=Equipment_serial_number)
        device_ty.value += 1
        device_ty.save()
        res = {
            "errorcode": 0,
            "content": {
                "id": d.id
            }
        }
        return JsonResponse(res)


class delete_one_device(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        device_id = request.data.get('device_id')
        dev = specific_device.objects.filter(id=device_id).first()
        dev_type = dev.type
        dev_type.value -= 1;
        dev_type.save()
        dev.is_active = False
        dev.save()
        return JsonResponse({"msg": "已删除", "status": 200})


class add_person_to_device(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        person_id = request.data.get('person_id')
        device_type_namelist = request.data.get('device_type_namelist')
        # print(device_type_namelist)
        per = user.objects.filter(id=person_id).first()
        person_to_device = person2device.objects.filter(person=per)
        for i in person_to_device:
            i.delete()
        for name in device_type_namelist:
            dev = device_type.objects.filter(name=name).first()
            if dev:
                x = person2device.objects.filter(person=per, device_type=dev)
                if x:
                    pass
                else:
                    person2device.objects.create(person=per, device_type=dev)
        res = {
            "errorcode": 0,
            "content": "授权成功"
        }
        return JsonResponse(res)


class start_device(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        person_id = request.data.get('person_id')
        device_id = request.data.get('device_id')
        per = user.objects.filter(id=person_id).first()
        dev = specific_device.objects.filter(id=device_id).first()
        if dev.status == "1":
            return JsonResponse({"msg": "该设备故障", "status": 400})
        elif dev.status == "2":
            return JsonResponse({"msg": "该设备已删除", "status": 400})
        else:
            ty = dev.type
            per2dev = person2device.objects.filter(person=per, device_type=ty).first()
            if not per2dev:
                return JsonResponse({"msg": "该用户无法使用此类设备", "status": 400})
            else:
                isrun_devList = device_running.objects.filter(device=dev)
                isrun_userList = device_running.objects.filter(person=per)
                if isrun_devList:
                    for isrun_dev in isrun_devList:
                        if not isrun_dev.end_time:
                            return JsonResponse({"msg": "该设备正在使用", "status": 400})
                if isrun_userList:
                    for isrun_user in isrun_userList:
                        if not isrun_user.end_time:
                            return JsonResponse({"msg": "该用户正在使用其他设备", "status": 400})
                x = device_running.objects.create(person=per, device=dev)
                res = {
                    "errorcode": 0,
                    "content": {
                        "starttime": x.start_time
                    }
                }
                return JsonResponse(res)


class end_device(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        person_id = request.data.get('person_id')
        device_id = request.data.get('device_id')
        per = user.objects.filter(id=person_id).first()
        dev = specific_device.objects.filter(id=device_id).first()
        list = device_running.objects.filter(person=per, device=dev)
        if not list:
            return JsonResponse({"msg": "该设备未使用或该人员未使用当前设备", "status": 400})
        else:

            for x in list:
                if not x.end_time:
                    x.end_time = datetime.datetime.now()
                    x.save()
                    res = {
                        "errorcode": 0,
                        "content": {
                            "endtime": x.end_time
                        }
                    }
                    return JsonResponse(res)

            return JsonResponse({"msg": "该设备未使用或该人员未使用当前设备", "status": 400})


class add_monitor_type(APIView):
    # authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        monitor_name = request.data.get('monitor_name')
        device_type_id = request.data.get('device_type_id')
        low_value = request.data.get('low_value')
        high_value = request.data.get('high_value')
        m = device_watch_type.objects.filter(name=monitor_name)
        if m:
            return JsonResponse({"msg": "已存在该名称的设备监控值类型", "status": 400})
        else:
            device_t = device_type.objects.filter(id=device_type_id).first()
            x = device_watch_type.objects.create(name=monitor_name, device_type=device_t, value_low=low_value,
                                                 value_hign=high_value)
            res = {
                "errorcode": 0,
                "content": {
                    "monitor_type_id": x.id
                }
            }
            return JsonResponse(res)


class error_upload(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        device_id = request.data.get('device_id')
        person_id = request.data.get('person_id')
        watch_id = request.data.get('watch_id')
        watch_value = request.data.get('watch_value')
        dev = specific_device.objects.filter(id=device_id).first()
        per = user.objects.filter(id=person_id).first()
        watch = device_watch_type.objects.filter(id=watch_id).first()
        r = device_running.objects.filter(person=per, device=dev)
        if not r:
            return JsonResponse({"msg": "该用户没有操作过此设备", "status": 400})
        else:
            device_exception.objects.create(device=dev, person=per, watch=watch, watch_value=watch_value)
            res = {
                "errorcode": 0,
                "content": {
                    "msg": "上报成功"
                }
            }
        return JsonResponse(res)


# 安全管理-----------------------------------start----------------------------------
class add_env_warn_type(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        env_warn_type_name = request.data.get('env_warn_type_name')
        warn_value = request.data.get('warn_value')
        if env_warn_type.objects.filter(name=env_warn_type_name).first():
            return JsonResponse({"msg": "已经存在此名称环境预警类型", "status": 400})
        else:
            env_warn_type.objects.create(name=env_warn_type_name, warn_value=warn_value)
            return JsonResponse({"msg": "增加成功", "status": 200})


class delete_env_warn_type(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        env_warn_type_name = request.data.get('env_warn_type_name')
        if not env_warn_type.objects.filter(name=env_warn_type_name).first():
            return JsonResponse({"msg": "没有此名称环境预警类型", "status": 400})
        else:
            env_warn_type.objects.filter(name=env_warn_type_name).first().delete()
            return JsonResponse({"msg": "删除成功", "status": 200})


class change_env_warn_type(APIView):
    authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        env_warn_type_id = request.data.get('env_warn_type_id')
        env_warn_type_name = request.data.get('env_warn_type_name')
        warn_value = request.data.get('warn_value')
        if not env_warn_type.objects.filter(warn_id=env_warn_type_id).first():
            return JsonResponse({"msg": "没有此环境预警类型", "status": 400})
        else:
            ewt = env_warn_type.objects.filter(warn_id=env_warn_type_id).first()
            ewt.name = env_warn_type_name
            ewt.warn_value = warn_value
            ewt.save()
            return JsonResponse({"msg": "修改成功", "status": 200})


class get_env_warn_type(APIView):
    # authentication_classes = [JwtQueryParamsAuthentication, ]

    def get(self, request):
        ewtOb = env_warn_type.objects.all()
        re = env_warn_typeSerializer(ewtOb, many=True)
        return Response({"data": re.data, "status": 200})


class add_env_exception(APIView):
    # authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        env_warn_type_id = request.data.get('env_warn_type_id')
        watch_value = request.data.get('watch_value')
        ewt = env_warn_type.objects.filter(warn_id=env_warn_type_id).first()
        ee = env_exception.objects.create(warn_type=ewt, watch_value=watch_value)
        if ee:
            return JsonResponse({"msg": "上报成功", "status": 200})
        else:
            return JsonResponse({"msg": "上报失败", "status": 400})


class get_env_exception(APIView):
    # authentication_classes = [JwtQueryParamsAuthentication, ]

    def get(self, request):
        eeob = env_exception.objects.all()
        res = []
        for ee in eeob:
            da = {
                "id": ee.id,
                "upload_time": ee.upload_time,
                "watch_value": ee.watch_value,
                "warn_type": ee.warn_type.name,
                "limit": ee.watch_value
            }
            res.append(da)

        return Response({"data": res, "status": 200})


class add_person_illegel_type(APIView):
    # authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        name = request.data.get('person_illegel_type_name')
        if person_illegel_type.objects.filter(name=name).first():
            return JsonResponse({"msg": "已经存在此名称人员违规操作类型", "status": 400})
        else:
            pit = person_illegel_type.objects.create(name=name)
            if not pit:
                return JsonResponse({"msg": "创建失败", "status": 400})
            else:
                return JsonResponse({"msg": "创建成功", "status": 200})


class delete_person_illegel_type(APIView):
    # authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        id = request.data.get('person_illegel_type_id')
        if not person_illegel_type.objects.filter(illegel_id=id).first():
            return JsonResponse({"msg": "没有该人员违规操作类型", "status": 400})
        else:
            pit = person_illegel_type.objects.filter(illegel_id=id).first().delete()
            if pit:
                return JsonResponse({"msg": "删除成功", "status": 200})
            else:
                return JsonResponse({"msg": "删除失败", "status": 400})


class get_person_illegel_type(APIView):
    # authentication_classes = [JwtQueryParamsAuthentication, ]

    def get(self, request):
        pit = person_illegel_type.objects.all()
        re = person_illegel_typeSerializer(pit, many=True)
        return Response({"data": re.data, "status": 200})


class add_person_illegel_upload(APIView):
    # authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        specific_device_id = request.data.get('specific_device_id')
        person_id = request.data.get('person_id')
        illegel_type_id = request.data.get('illegel_type_id')
        sd = specific_device.objects.filter(id=specific_device_id).first()
        per = user.objects.filter(id=person_id).first()
        pit = person_illegel_type.objects.filter(illegel_id=illegel_type_id).first()
        piu = person_illegel_upload.objects.create(device=sd, person=per, illegel_type=pit)
        if not piu:
            return JsonResponse({"msg": "上报失败", "status": 400})
        else:
            return JsonResponse({"msg": "上报成功", "status": 200})


class get_person_illegel_upload(APIView):
    # authentication_classes = [JwtQueryParamsAuthentication, ]

    def get(self, request):
        piuList = person_illegel_upload.objects.all()
        res = []
        for piu in piuList:
            da = {
                "id": piu.id,
                "upload_time": piu.upload_time,
                "device": piu.device.type.name + "-id:" + str(
                    piu.device.id) + "-编号：" + piu.device.Equipment_serial_number,
                "person": piu.person.realname,
                "illegel_type": piu.illegel_type.name
            }
            res.append(da)

        return Response({"data": res, "status": 200})


class delete_person_illegel_upload(APIView):
    # authentication_classes = [JwtQueryParamsAuthentication, ]

    def post(self, request):
        person_illegel_upload_id = request.data.get('person_illegel_upload_id')
        piu = person_illegel_upload.objects.filter(id=person_illegel_upload_id).first()
        if not piu:
            return JsonResponse({"msg": "没有该记录", "status": 400})
        else:
            piu.delete()
            return JsonResponse({"msg": "删除成功", "status": 200})


# 安全管理-----------------------------------end----------------------------------


#     下载xlsx demo
class downloadxlsxdemo(APIView):
    # authentication_classes = [JwtQueryParamsAuthentication, ]
    def get(self, request):
        the_file_name = 'demoUploduser.xlsx'
        filename = 'E:/File_my/SmartMine/smartmine_django/static/' + the_file_name

        response = StreamingHttpResponse(readFile(filename))
        response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
        return response


def readFile(filename, chunk_size=512):
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break
