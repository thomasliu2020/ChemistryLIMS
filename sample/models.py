from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from adminpro.utils.common import upload_direct_path
from adminpro.fields.sample import RestrictedFileField, generate_sample_no


# Create your models here.


class SampleLog(models.Model):
    '''
    样品登记簿
    '''
    region = models.CharField(u'分地点代码', max_length=12, null=True, blank=True, )
    sample_no = models.CharField(u'样品编号', max_length=18, null=True, blank=True,
                                 help_text="系统自动创建: 月份(2位)+流水号+分地点代码(2~3位)+随机字符(1~2位)+年代号后2位,总计12位")
    report_no = models.CharField(u'报告编号', max_length=24, null=True, blank=True)
    order_no = models.CharField(u'委托单号', max_length=24, null=True, blank=True)
    name = models.CharField(u'样品名称', max_length=48, null=True, blank=True)
    client = models.CharField(u'委托单位', max_length=128, null=True, blank=True)
    sampling = models.DateField(u"取样日期", auto_now=False, null=True, blank=True)
    reception = models.DateField(u"接收日期", default=timezone.now)
    time = models.TimeField(u"接收时间", default=timezone.now, null=True)
    description = models.CharField(u'状态描述', max_length=256, null=True, blank=True, help_text=u"外观,标识信息等...")
    grade = models.CharField(u'样品规格', max_length=32, null=True, blank=True)
    register = models.CharField(u'收样人', max_length=32, null=True, blank=True)
    remark = models.CharField(u'备注', null=True, blank=True, max_length=256)
    sub_fee = models.FloatField(u"分包费", null=True, blank=True, default=0)
    delivery_fee = models.SmallIntegerField(u"送样费", null=True, blank=True, default=0)
    is_checked = models.BooleanField(default=False, verbose_name='复核', )
    checked_by = models.ForeignKey(User, null=True, related_name='sample_logbook', on_delete=models.SET_NULL)
    report = RestrictedFileField(upload_to=upload_direct_path, blank=True, null=True, verbose_name='测试报告',
                                 max_length=100,
                                 content_types=['application/pdf', 'application/zip'],
                                 max_upload_size=5242880,
                                 help_text="请以PDF或ZIP格式上传")

    list_filter = ("region", "reception")
    search_fields = ("sample_no", "report_no", "client", "name")

    def __str__(self):
        return "%s" % self.sample_no

    def save(self, *args, **kwargs):
        if not self.pk:
            self.sample_no = generate_sample_no(self, max_length=12)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "样品登记"
        verbose_name_plural = verbose_name
        db_table = "sample_log"


class TestLogManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_display=True)


class TestLog(models.Model):
    '''
    测试登记簿
    '''
    sample = models.ForeignKey(SampleLog, verbose_name="样品信息",
                               related_name="test_logbook", on_delete=models.CASCADE, )
    item = models.CharField(max_length=32, null=True, blank=False, verbose_name="检测项目", )
    method = models.CharField(max_length=64, null=True, blank=True, verbose_name="测试方法", )
    date = models.DateField(u"检测日期", default=timezone.now, null=True)
    completed = models.DateField(u"结束日期", auto_now_add=True, null=True, blank=True)
    type = models.SmallIntegerField(choices=((1, "正常业务"), (0, "分包"), (2, "质控")), default=1, verbose_name='测试类型')
    result = models.CharField(max_length=64, null=True, blank=True, verbose_name='结果')
    unit = models.CharField(max_length=32, default='-', null=True, blank=True, )
    spec = models.CharField(max_length=64, null=True, blank=True)
    chemist = models.CharField(max_length=6, null=True, blank=True, verbose_name="检测人员", help_text='分包项目可用“分包”代替')
    score = models.DecimalField(decimal_places=1, max_digits=2, default=1.0, verbose_name="绩效分",
                                help_text="计件制用来计算员工工作量的数据")
    allowance = models.PositiveIntegerField(default=5, help_text="计件制用来计算员工绩效补贴的数据,默认为5元")
    is_kpi = models.BooleanField(default=True, null=True, blank=True, verbose_name="是否计入KPI,选择否将不计入绩效")
    is_display = models.BooleanField(default=True, null=True, blank=True, verbose_name="是否显示,代替硬删除")
    objects = TestLogManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "测试管理"
        verbose_name_plural = verbose_name
        db_table = "test_log"
