from django.db import models
from django.contrib.auth.models import User
from method.models import MethodAbilityPrice


# Create your models here.
class ProductList(models.Model):
    name = models.CharField(max_length=128, verbose_name='产品规范')
    client = models.CharField(max_length=128, verbose_name="规范标签", help_text="客户名称，CMA/CNAS认可产品等")
    component = models.ForeignKey(to='ProductList', blank=True, null=True, verbose_name='组合规范', on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='template_create')
    is_confirmed = models.BooleanField(default=False)
    confirmed_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                     related_name='template_confirm')
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now_add=True)
    upload = models.FileField(verbose_name='资源上传', max_length=128, blank=True, null=True, upload_to="product/")
    equip_std_info = models.TextField(verbose_name='设备/标准物质编号', null=True, blank=True)

    def __str__(self):
        return "%s:%s" % (self.name, self.client)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '产品列表'
        verbose_name_plural = verbose_name
        db_table = "product_list"
        unique_together = ['name', 'client']


class Specification(models.Model):
    template = models.ForeignKey(ProductList, on_delete=models.CASCADE, related_name='specification', )
    component_id = models.SmallIntegerField(null=True, blank=True, verbose_name='组合模板id')
    test_item = models.CharField(max_length=64, verbose_name='项目', )
    method = models.ForeignKey(MethodAbilityPrice, null=True, on_delete=models.SET_NULL, related_name='method_2_spec')
    is_cma = models.BooleanField(verbose_name='CMA', default=False)
    is_cnas = models.BooleanField(verbose_name='CNAS', default=False)
    unit = models.CharField(max_length=32, default='-', null=True, blank=True, )
    specification = models.CharField(max_length=64, default='-', null=True, blank=True)
    reference_price = models.SmallIntegerField(null=True, blank=True, verbose_name='参考价格')
    score = models.FloatField(default=1.0)  # 无需显示并编辑
    allowance = models.SmallIntegerField(default=9)  # 无需显示并编辑
    manual_update = models.BooleanField(default=False, help_text="手动更新数据时勾选", verbose_name='手动更新')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s:%s" % (self.template.name, self.template.client)

    class Meta:
        verbose_name = '模板*资质*报价管理'
        verbose_name_plural = verbose_name
        unique_together = ['template_id', 'test_item']
