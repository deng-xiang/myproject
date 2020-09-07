from django.db import models
import datetime
import  django.utils.timezone as timezone
# Create your models here.
class Project(models.Model):
    STATUS_ITEMS=[
        (0,'申请'),
        (1,'进行'),
        (2,'归档'),
        (3,'作废')
    ]
    PROJECT_TYPES=[
        (0,'安全检查'),
        (1,'风险评估'),
        (2,'等保测评'),
        (3,'定额造价')
    ]
    name = models.CharField(max_length=128, verbose_name="项目名称")
    types = models.IntegerField(choices=PROJECT_TYPES,default=0,verbose_name="项目分类")
    create_time=models.DateField(auto_now_add=True,editable=False,verbose_name="创建时间")
    start_time=models.DateField(verbose_name="开始时间",null=True,blank=True)
    close_time=models.DateField(verbose_name="结束时间",null=True)
    status=models.IntegerField(choices=STATUS_ITEMS,default=0, verbose_name="项目状态")
    def __str__(self):
        return '<项目:{}>'.format(self.name)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        verbose_name=verbose_name_plural="项目信息"