from django.db import models
from equipment.models import EquipmentList
from adminpro.utils.common import upload_direct_path
from django.contrib.auth.models import User


# Create your models here.

class MethodAbilityPrice(models.Model):
    grade = (
        (0, '国际标准'),
        (1, '国家标准'),
        (2, '行业标准'),
        (3, '部门标准'),
        (4, '地方标准'),
        (5, '企标'),
        (6, 'SOP'),
        (7, '其他'),
    )
    parameters = models.CharField(u'参数名称', max_length=128, blank=True, null=True)
    parameters_en = models.CharField(u'参数名称（英）', max_length=128, blank=True, null=True)
    code = models.CharField(u'方法号', max_length=64, blank=True, null=True, )
    version = models.CharField(u'版本号', max_length=64, blank=True, null=True)
    method_code = models.CharField(u'方法号', max_length=64, blank=True, null=True)
    method_cn = models.CharField(u'方法名称(中)', max_length=512, blank=True, null=True)
    method_en = models.CharField(u'方法名称(英)', max_length=512, blank=True, null=True)
    method_grade = models.SmallIntegerField(u"标准级别", choices=grade, null=True, blank=True, )
    date_issued = models.DateField(u"发布日期", null=True, blank=True)
    date_implemented = models.DateField(u"实施日期", null=True, blank=True)
    status = models.CharField(u'版本状态', max_length=16, choices=(('valid', '现行'),
                                                               ('expired', '过期'),
                                                               ('to_implement', '即将实施')), default='valid')
    file = models.FileField(upload_to='method/', null=True, blank=True, verbose_name='在线查看')
    alternative_name = models.CharField(max_length=264, blank=True, null=True, default="N/A", verbose_name='参数别名')
    sub_parameter = models.CharField(max_length=264, blank=True, null=True, verbose_name='分参数', default='N/A')
    method_equivalent = models.CharField(max_length=128, blank=True, null=True, verbose_name='可替代方法')

    category_choice_value = (
        ('通用', '通用'),
        ('石油产品', '石油产品'),
        ('工业用油', '工业用油'),
        ('生物柴油', '生物柴油'),
        ('车用尿素', '车用尿素'),
        ('有机化工产品', '有机化工产品'),
        ('无机化工产品', '无机化工产品'),
        ('水质', '水质'),
        ('气体', '气体'),
        ('沥青', '沥青'),
        ('其他', '其他'),
    )
    category = models.CharField(choices=category_choice_value, verbose_name='基质', default='石油产品', max_length=128)

    ##########报价信息
    sample_size = models.SmallIntegerField(null=True, blank=True, verbose_name="最小检测用量(ml/g)")
    tat = models.SmallIntegerField(null=True, blank=True, verbose_name="检测时间(h)")
    price = models.PositiveIntegerField(null=True, blank=True, default=200, verbose_name="标准价格")
    bind_item = models.BooleanField(verbose_name="是否绑定", default=False)
    subcontract = models.BooleanField(verbose_name="是否分包", default=False)
    note = models.CharField(max_length=64, null=True, blank=True, verbose_name='报价说明')
    validation = models.CharField(choices=(("validated", "具备能力"),
                                           ("NA", "不具备")), default="validated", max_length=12)

    def __str__(self):
        return "%s:%s" % (self.parameters, self.method_code,)

    class Meta:
        verbose_name = "方法价目表"
        verbose_name_plural = verbose_name
        db_table = 'method_price'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Validation(models.Model):
    method = models.ForeignKey(MethodAbilityPrice, null=True, on_delete=models.SET_NULL, related_name='method_validation')
    location = models.CharField(verbose_name="分地点代码", default="CS", max_length=5)
    date = models.DateField(verbose_name="完成日期", auto_now=False)
    equip_info = models.ForeignKey(EquipmentList, verbose_name='设备信息', null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name="method_validation")
    equip_std_info = models.CharField(verbose_name='设备/标准物质编号', max_length=512, null=True, blank=True)
    validated_by = models.CharField(max_length=24, verbose_name="开发人", null=True)
    approved = models.ForeignKey(User, verbose_name="开发人", on_delete=models.SET_NULL, null=True,
                                 related_name="method_validation")
    upload = models.FileField(upload_to=upload_direct_path, blank=True, null=True, verbose_name='验证资料')

    class Meta:
        verbose_name = "方法验证"
        verbose_name_plural = verbose_name
        db_table = 'method_validation'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
