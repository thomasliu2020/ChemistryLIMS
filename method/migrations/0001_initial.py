# Generated by Django 4.0 on 2021-12-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MethodAbilityPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', models.CharField(blank=True, max_length=128, null=True, verbose_name='参数名称')),
                ('parameters_en', models.CharField(blank=True, max_length=128, null=True, verbose_name='参数名称（英）')),
                ('code', models.CharField(blank=True, max_length=64, null=True, verbose_name='方法号')),
                ('version', models.CharField(blank=True, max_length=64, null=True, verbose_name='版本号')),
                ('method_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='方法号')),
                ('method_cn', models.CharField(blank=True, max_length=512, null=True, verbose_name='方法名称(中)')),
                ('method_en', models.CharField(blank=True, max_length=512, null=True, verbose_name='方法名称(英)')),
                ('method_grade', models.SmallIntegerField(blank=True, choices=[(0, '国际标准'), (1, '国家标准'), (2, '行业标准'), (3, '部门标准'), (4, '地方标准'), (5, '企标'), (6, 'SOP'), (7, '其他')], null=True, verbose_name='标准级别')),
                ('date_issued', models.DateField(blank=True, null=True, verbose_name='发布日期')),
                ('date_implemented', models.DateField(blank=True, null=True, verbose_name='实施日期')),
                ('status', models.CharField(choices=[('valid', '现行'), ('expired', '过期'), ('to_implement', '即将实施')], default='valid', max_length=16, verbose_name='版本状态')),
                ('file', models.FileField(blank=True, null=True, upload_to='method/', verbose_name='在线查看')),
                ('category', models.CharField(choices=[('通用', '通用'), ('石油产品', '石油产品'), ('工业用油', '工业用油'), ('生物柴油', '生物柴油'), ('车用尿素', '车用尿素'), ('有机化工产品', '有机化工产品'), ('无机化工产品', '无机化工产品'), ('水质', '水质'), ('气体', '气体'), ('沥青', '沥青'), ('其他', '其他')], default='石油产品', max_length=128, verbose_name='基质')),
                ('validation', models.CharField(choices=[('validated', '具备能力'), ('in progress', '开发中'), ('NA', '不具备')], default='validated', max_length=12)),
                ('alternative_name', models.CharField(blank=True, default='N/A', max_length=264, null=True, verbose_name='参数别名')),
                ('sub_parameter', models.CharField(blank=True, default='N/A', max_length=264, null=True, verbose_name='分参数')),
                ('method_equivalent', models.CharField(blank=True, max_length=128, null=True, verbose_name='可替代方法')),
                ('remark', models.CharField(blank=True, max_length=128, null=True, verbose_name='技术性说明')),
                ('sample_size', models.SmallIntegerField(blank=True, null=True, verbose_name='最小检测用量(ml/g)')),
                ('tat', models.SmallIntegerField(blank=True, null=True, verbose_name='检测时间(h)')),
                ('price', models.PositiveIntegerField(blank=True, default=200, null=True, verbose_name='标准价格')),
                ('bind_item', models.BooleanField(default=False, verbose_name='是否绑定')),
                ('subcontract', models.BooleanField(default=False, verbose_name='是否分包')),
                ('note', models.CharField(blank=True, max_length=64, null=True, verbose_name='报价说明')),
            ],
            options={
                'verbose_name': '方法*能力*价格',
                'verbose_name_plural': '方法*能力*价格',
                'db_table': 'method_capability_price',
            },
        ),
    ]