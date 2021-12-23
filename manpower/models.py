from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class GeneralStaffList(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, unique=True, verbose_name='姓名')
    staff_id = models.CharField(max_length=8, blank=True, null=True, unique=True, verbose_name='工号')
    birthday = models.DateField("出生日期", null=True, blank=True)
    age = models.SmallIntegerField(blank=True, null=True)
    identity_no = models.CharField(max_length=20, blank=True, null=True, unique=True, verbose_name='身份号')
    qualification = models.CharField("职称", blank=True, null=True, max_length=8)
    gender = models.CharField("性别", choices=(('male', "男"), ('female', "女")), max_length=6)
    degree = models.CharField("文化程度", null=True, blank=True, max_length=16)
    major = models.CharField("所学专业", null=True, blank=True, max_length=16)
    graduated_time = models.DateField("毕业时间", null=True, blank=True)
    date_joined = models.DateField("入职日期", null=True, blank=True)
    years_post = models.SmallIntegerField("本岗位年限", blank=True, null=True)
    remark = models.CharField("备注", max_length=16, null=True, blank=True)
    user_name = models.OneToOneField(User, verbose_name="用户", related_name='general_staff_list',
                                     on_delete=models.CASCADE)
    region = models.CharField(verbose_name='地区', null=True, blank=True, max_length=8)
    supervisor = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL, verbose_name="上级主管",
                                   related_name='sub_class_staffs')
    resign_date = models.DateField("离职日期", null=True, blank=True)
    tags = models.CharField(choices=(('management', '管理人员'),
                                     ('technical', '技术人员'),
                                     ('sales', '销售'),
                                     ('admin', '办公室人员'),
                                     ('others', '合作伙伴')), max_length=12, blank=True, null=True)

    certificate_sn = models.CharField(verbose_name="岗位资格证书编号", max_length=12, null=True, blank=True)
    certificate = models.FileField(verbose_name="岗位资格证书", upload_to="hr/certificate/", null=True, blank=True)

    def __str__(self):
        full_name = self.user_name.last_name + self.user_name.first_name
        return full_name

    class Meta:
        verbose_name = "人员总表"
        verbose_name_plural = verbose_name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert=False, force_update=False, using=None,
                     update_fields=None)
