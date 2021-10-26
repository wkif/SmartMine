# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 21:51
# @Author  : kif
# @FileName: serializers.py
# @Software: PyCharm
from rest_framework import serializers
from .models import *


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'realname', 'username', 'age', 'gender', 'avatar', 'phone', 'country', 'province', 'city',
                  'userEmail', 'work_id', 'work_id', 'is_formal', 'status', 'is_comp_rest', 'base_salary', 'user_type']


class specific_deviceSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = specific_device
        fields = '__all__'

    def get_type(self, obj):
        return obj.type.name


class device_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = device_type
        fields = '__all__'


class env_warn_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = env_warn_type
        fields = '__all__'

class person_illegel_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = person_illegel_type
        fields = '__all__'

