from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class QualityDocument(models.Model):
    category_choice = (
        ("质量手册", "质量手册"),
        ("程序文件", "程序文件"),
        ("作业指导书", "作业指导书"),
        ("质量记录表格", "质量记录表格"),
    )
    file_no = models.CharField(max_length=36, blank=True, null=True, verbose_name='文件编号')
    title = models.CharField(max_length=36, blank=True, null=True, verbose_name='文件名称')
    category = models.CharField(choices=category_choice, verbose_name='文件类别', default='作业指导书', max_length=36)
    tags = models.CharField(max_length=24, blank=True, null=True, verbose_name='标签')
    version = models.CharField(max_length=12, blank=True, null=True, verbose_name='版次')
    editor = models.CharField(max_length=12, blank=True, null=True, verbose_name='编写')
    checked_by = models.CharField(max_length=12, blank=True, null=True, verbose_name='审核')
    issued_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='批准', related_name="quality_issued")
    issued_date = models.DateField(auto_now=False, verbose_name='颁布日期', null=True, blank=True)
    changed_date = models.DateField(auto_now=False, verbose_name='修改日期', null=True, blank=True)
    status = models.CharField('受控状态', max_length=16, choices=(('controlled', '受控'),
                                                              ('uncontrolled', '非受控')), default='uncontrolled')
    upload = models.FileField(upload_to='quality_document/', null=True, blank=True, verbose_name='在线资源')

    list_filter = ("category", "status", "changed_date")
    search_fields = ("file_no", "title", "editor")

    def __str__(self):
        return "%s: %s" % (self.file_no, self.title)

    class Meta:
        verbose_name = "质量体系文件管理"
        verbose_name_plural = verbose_name
        db_table = "quality_document"
        unique_together = ['file_no', 'version']
