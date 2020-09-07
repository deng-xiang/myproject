# Generated by Django 3.1.1 on 2020-09-07 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='项目名称')),
                ('types', models.IntegerField(choices=[(0, '安全检查'), (1, '风险评估'), (2, '等保测评'), (3, '定额造价')], default=0, verbose_name='项目分类')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('start_time', models.DateField(blank=True, null=True, verbose_name='开始时间1')),
                ('close_time', models.DateField(null=True, verbose_name='结束时间')),
                ('status', models.IntegerField(choices=[(0, '申请'), (1, '进行'), (2, '归档'), (3, '作废')], default=0, verbose_name='项目状态')),
            ],
            options={
                'verbose_name': '项目信息',
                'verbose_name_plural': '项目信息',
            },
        ),
    ]
