import datetime

from django.db import models


# Create your models here.

# 人员管理   ----------------------------------------------start------------------------

class organization_structure(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('组织架构名称', max_length=50)
    brief = models.CharField('组织架构简介', null=True, blank=True, max_length=500)

    class Meta:
        db_table = '组织架构表'
        verbose_name = "组织架构表"
        verbose_name_plural = "组织架构表"

    def __str__(self):
        return self.name


class position(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('职位名称', max_length=50)
    org_id = models.ForeignKey("organization_structure", on_delete=models.CASCADE, default='')

    class Meta:
        db_table = '职位表'
        verbose_name = "职位表"
        verbose_name_plural = "职位表"

    def __str__(self):
        return self.name


class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default='')
    realname = models.CharField(max_length=50, default='')
    age = models.CharField(max_length=3, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    gender = models.CharField(max_length=2, default='未知')
    avatar = models.CharField(max_length=200, default="https://api.sunweihu.com/api/sjtx/api.php?lx=a1")
    phone = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    province = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    userEmail = models.EmailField(default='')
    induction_date = models.DateField('注册日期', auto_now_add=True)
    # department = models.CharField(max_length=20, default='')
    work_id = models.ForeignKey("position", on_delete=models.CASCADE, default='', null=True, blank=True)
    is_formal = models.BooleanField('是否已转正', default=False)
    status_CHOICES = (
        (1, u'已离职'),
        (0, u'正常'),
    )
    status = models.IntegerField(choices=status_CHOICES, default=0)
    is_comp_rest = models.BooleanField('是否签订竞业限制', blank=True, null=True)
    base_salary = models.IntegerField('基本工资', default=0)
    user_type = models.CharField(max_length=4, default='普通成员')

    class Meta:
        db_table = '用户'
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.realname


class salary_pay(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user', on_delete=models.CASCADE, default='')
    date = models.DateField('发放时间', auto_now_add=True)
    salary = models.IntegerField('发放金额', default=0)
    type_CHOICES = (
        (0, u'基本工资'),
        (1, u'年终奖')
    )
    type = models.IntegerField(choices=type_CHOICES, default=0)

    class Meta:
        db_table = '工资发放表'
        verbose_name = "工资发放表"
        verbose_name_plural = "工资发放表"


class leave_record(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user', on_delete=models.CASCADE, default='')
    start_time = models.TimeField('请假开始时间', auto_now_add=True)
    end_time = models.TimeField('请假结束时间', null=True, blank=True)
    description = models.CharField('原因', default='', max_length=500)

    class Meta:
        db_table = '请假记录表'
        verbose_name = "请假记录表"
        verbose_name_plural = "请假记录表"


class overtime_approval(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user', on_delete=models.CASCADE, default='')
    start_time = models.TimeField('加班申请开始时间', auto_now_add=True)
    end_time = models.TimeField('加班申请结束时间', null=True, blank=True)
    description = models.CharField('原因', default='', max_length=500)

    class Meta:
        db_table = '加班审批表'
        verbose_name = "加班审批表"
        verbose_name_plural = "加班审批表"


class punch_record(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user', on_delete=models.CASCADE, default='')
    card_time = models.TimeField('打卡时间', auto_now_add=True)

    class Meta:
        db_table = '打卡记录表'
        verbose_name = "打卡记录表"
        verbose_name_plural = "打卡记录表"


class evaluation(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user', related_name='user', on_delete=models.CASCADE, default='')
    eva_time = models.TimeField('考核时间', auto_now_add=True)
    eva_grade = models.CharField(default='', max_length=4)
    #     A/B/C/D
    eva_id = models.ForeignKey('user', related_name='eva_id', on_delete=models.CASCADE, default='')
    content = models.CharField('考核评价内容', default='', max_length=4)

    class Meta:
        db_table = '考核评价表'
        verbose_name = "考核评价表"
        verbose_name_plural = "考核评价表"


class training_time(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('名称', default='', max_length=200)
    talk_id = models.ForeignKey('user', on_delete=models.CASCADE, default='')
    start_time = models.TimeField('培训开始时间', auto_now_add=True)
    end_time = models.TimeField('培训结束时间', null=True, blank=True)

    class Meta:
        db_table = '培训时间表'
        verbose_name = "培训时间表"
        verbose_name_plural = "培训时间表"

    def __str__(self):
        return self.name


class attend_training(models.Model):
    id = models.AutoField(primary_key=True)
    train_id = models.ForeignKey('training_time', on_delete=models.CASCADE, default='')
    person_id = models.ForeignKey('user', on_delete=models.CASCADE, default='')

    class Meta:
        db_table = '培训参加表'
        verbose_name = "培训参加表"
        verbose_name_plural = "培训参加表"


# 人员管理   ----------------------------------------------end------------------------

# 设备管理   ----------------------------------------------start------------------------


# 具体设备表
class specific_device(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey("device_type", on_delete=models.CASCADE, default='')
    status_CHOICES = (
        (0, u'正常'),
        (1, u'故障'),
        (2, u'维修中')
    )
    status = models.CharField(choices=status_CHOICES, default=0, max_length=4)
    Equipment_serial_number = models.CharField(max_length=255, default='', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    Running_state_CHOICES = (
        (1, u'运行中'),
        (0, u'休息'),
    )
    Running_state = models.CharField(choices=Running_state_CHOICES, default=0, max_length=4)

    class Meta:
        db_table = '具体设备表'
        verbose_name = "具体设备表"
        verbose_name_plural = "具体设备表"

    def __str__(self):
        return self.type.name + "-" + str(self.id)


# 人员设备表
class person2device(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey("user", on_delete=models.CASCADE, default='')
    device_type = models.ForeignKey("device_type", on_delete=models.CASCADE, default='')

    class Meta:
        db_table = '人员设备表'
        verbose_name = "人员设备表"
        verbose_name_plural = "人员设备表"


# 设备类型
class device_type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='')
    brief = models.CharField(max_length=500, default='', null=True, blank=True)
    value = models.IntegerField(default=0)

    class Meta:
        db_table = '设备类型'
        verbose_name = "设备类型"
        verbose_name_plural = "设备类型"

    def __str__(self):
        return self.name


# 设备运行表
class device_running(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey("user", on_delete=models.CASCADE, default='')
    device = models.ForeignKey("specific_device", on_delete=models.CASCADE, default='')
    start_time = models.DateTimeField('开始运行时间', auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = '设备运行表'
        verbose_name = "设备运行表"
        verbose_name_plural = "设备运行表"


# 设备监控值类型表
class device_watch_type(models.Model):
    id = models.AutoField(primary_key=True)
    device_type = models.ForeignKey("device_type", on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=50, default='')
    value_low = models.IntegerField(default=0)
    value_hign = models.IntegerField(default=100)

    class Meta:
        db_table = '设备监控值类型表'
        verbose_name = "设备监控值类型表"
        verbose_name_plural = "设备监控值类型表"

    def __str__(self):
        return self.name + "(" + str(self.value_low) + "-" + str(self.value_hign) + ")"


# 设备异常上报表
class device_exception(models.Model):
    id = models.AutoField(primary_key=True)
    upload_time = models.DateField('上报时间', auto_now_add=True)
    device = models.ForeignKey("specific_device", on_delete=models.CASCADE)
    person = models.ForeignKey("user", on_delete=models.CASCADE, default='')
    watch = models.ForeignKey("device_watch_type", on_delete=models.CASCADE, default='')
    watch_value = models.IntegerField(default='')

    class Meta:
        db_table = '设备异常上报表'
        verbose_name = "设备异常上报表"
        verbose_name_plural = "设备异常上报表"


# 设备管理   ----------------------------------------------end------------------------


# 安全管理-----------------------------------start----------------------------------

class env_warn_type(models.Model):
    warn_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    warn_value = models.CharField(max_length=50, default='')

    class Meta:
        db_table = '环境预警类型表'
        verbose_name = "环境预警类型表"
        verbose_name_plural = "环境预警类型表"


class env_exception(models.Model):
    id = models.AutoField(primary_key=True)
    upload_time = models.DateTimeField('上报时间', auto_now_add=True)
    warn_type = models.ForeignKey("env_warn_type", on_delete=models.CASCADE, default='')
    watch_value = models.CharField(max_length=50, default='')

    class Meta:
        db_table = '环境预警上报表'
        verbose_name = "环境预警上报表"
        verbose_name_plural = "环境预警上报表"


class person_illegel_type(models.Model):
    illegel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')

    class Meta:
        db_table = '人员违规操作类型'
        verbose_name = "人员违规操作类型"
        verbose_name_plural = "人员违规操作类型"


class person_illegel_upload(models.Model):
    id = models.AutoField(primary_key=True)
    upload_time = models.DateTimeField('上报时间', auto_now_add=True)
    device = models.ForeignKey('specific_device', on_delete=models.CASCADE, default='')
    person = models.ForeignKey('user', on_delete=models.CASCADE, default='')
    illegel_type = models.ForeignKey('person_illegel_type', on_delete=models.CASCADE, default='')

    class Meta:
        db_table = '人员违规操作上报'
        verbose_name = "人员违规操作上报"
        verbose_name_plural = "人员违规操作上报"


# class person_illegel_upload(models.Model):
#     id = models.AutoField(primary_key=True)
#     upload_time = models.DateTimeField('上报时间', auto_now_add=True)
#     device = models.ForeignKey('specific_device', on_delete=models.CASCADE, default='')
#     person = models.ForeignKey('user', on_delete=models.CASCADE, default='')
#     illgel = models.ForeignKey('person_illegel_type', on_delete=models.CASCADE, default='')
#
#     class Meta:
#         db_table = '人员违规操作上报'
#         verbose_name = "人员违规操作上报"
#         verbose_name_plural = "人员违规操作上报"


# 安全管理-----------------------------------end----------------------------------


# 邮箱验证
class EmailVerifyRecord(models.Model):
    # 验证码
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    # 包含注册验证和找回验证
    send_type = models.CharField(verbose_name="验证码类型", max_length=20,
                                 choices=(("register", "注册"), ("forget", "找回密码"), ("changeEmail", "修改邮箱")))
    send_time = models.DateTimeField(verbose_name="发送时间", default=datetime.datetime.now())

    class Meta:
        db_table = '邮箱验证码'
        verbose_name = u" 邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)
# python manage.py makemigrations
# python manage.py migrate
