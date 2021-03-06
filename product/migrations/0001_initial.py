# Generated by Django 4.0 on 2021-12-22 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('method', '0002_alter_methodabilityprice_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='产品规范')),
                ('client', models.CharField(help_text='客户名称，CMA/CNAS认可产品等', max_length=128, verbose_name='规范标签')),
                ('is_confirmed', models.BooleanField(default=False)),
                ('created_date', models.DateField(auto_now=True)),
                ('updated_date', models.DateField(auto_now_add=True)),
                ('upload', models.FileField(blank=True, max_length=128, null=True, upload_to='product/', verbose_name='资源上传')),
                ('equip_std_info', models.TextField(blank=True, null=True, verbose_name='设备/标准物质编号')),
                ('component', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.productlist', verbose_name='组合规范')),
                ('confirmed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='template_confirm', to='auth.user')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='template_create', to='auth.user')),
            ],
            options={
                'verbose_name': '产品列表',
                'verbose_name_plural': '产品列表',
                'db_table': 'product_list',
                'unique_together': {('name', 'client')},
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_id', models.SmallIntegerField(blank=True, null=True, verbose_name='组合模板id')),
                ('test_item', models.CharField(max_length=64, verbose_name='项目')),
                ('is_cma', models.BooleanField(default=False, verbose_name='CMA')),
                ('is_cnas', models.BooleanField(default=False, verbose_name='CNAS')),
                ('unit', models.CharField(blank=True, default='-', max_length=32, null=True)),
                ('specification', models.CharField(blank=True, default='-', max_length=64, null=True)),
                ('reference_price', models.SmallIntegerField(blank=True, null=True, verbose_name='参考价格')),
                ('score', models.FloatField(default=1.0)),
                ('allowance', models.SmallIntegerField(default=9)),
                ('manual_update', models.BooleanField(default=False, help_text='手动更新数据时勾选', verbose_name='手动更新')),
                ('method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='method_2_spec', to='method.methodabilityprice')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='product.productlist')),
            ],
            options={
                'verbose_name': '模板*资质*报价管理',
                'verbose_name_plural': '模板*资质*报价管理',
                'unique_together': {('template_id', 'test_item')},
            },
        ),
    ]
