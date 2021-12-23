from django.db import models
from method.models import MethodAbilityPrice
from django.contrib.auth.models import User


# Create your models here.

class QualityControlPlan(models.Model):
    tools = (
        (0, '能力验证'),
        (1, '数理统计'),
        (2, '使用标准物质'),
        (3, '实验室间比对'),
        (4, '仪器比对'),
        (5, '方法比对'),
        (6, '人员比对'),
        (7, '留样再测'),
        (8, '不同检测结果的相关性'),
    )
    choices = (('daily', '日检'),
               ('weekly', '周检'),
               ('monthly', '月检'),
               ('quarterly', '季检'),
               ('half a year', '半年检'),
               ('yearly', '年检'),
               ('each batch', '每批次'),
               ('others', '其他'),
               )

    parameter = models.ForeignKey(MethodAbilityPrice, verbose_name='质控项目',
                                  related_name="quality_control_plan", on_delete=models.CASCADE, )
    serial_no = models.CharField(verbose_name='序号', max_length=8, null=True, blank=True)
    qc_tools = models.SmallIntegerField(verbose_name="质控手段", choices=tools, null=True, blank=True, default=1)
    frequency = models.CharField(max_length=12, choices=choices, default='each batch', verbose_name='频次要求')
    controlled_by = models.ForeignKey(User, verbose_name="项目负责人",
                                      related_name="quality_control_plan", on_delete=models.CASCADE,
                                      limit_choices_to={'general_staff_list__tags': 'technical'})
    date = models.DateField(verbose_name="更新日期", auto_now_add=True)
    location_code = models.CharField(max_length=8, default='CS')
    equipment = models.CharField(max_length=36, verbose_name='设备', null=True, blank=True)
    group = models.CharField(max_length=24, verbose_name='组别', null=True, blank=True)
    state = models.SmallIntegerField(verbose_name='质控评分', default=7, )
    is_controlled = models.BooleanField(verbose_name='质控中', default=True, help_text='不在控制中或者失效时用来代替删除')

    ####获取关联表格信息，避免跨表查询与计算

    def __str__(self):
        return "%s (%s)-%s" % (self.parameter, self.location_code, self.get_qc_tools_display())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "质控计划"
        verbose_name_plural = verbose_name
        ordering = ['serial_no', ]
