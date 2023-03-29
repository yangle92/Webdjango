from django.db import models

# Create your models here.

class Person(models.Model):
    name =  models.CharField('姓名',max_length=30)
    age = models.IntegerField('年龄')
    sex_choices=(
        (1,'男'),
        (2,'女'),
    )
    sex=models.IntegerField('性别',choices=sex_choices,default=1)
    birthday=models.DateField('出生日期',null=True)
    update_time=models.DateTimeField('更新时间',auto_now_add=True,null=True)