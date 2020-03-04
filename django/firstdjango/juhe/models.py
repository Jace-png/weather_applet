from django.db import models

# Create your models here.
class User(models.Model):
    #openid
    openid = models.CharField(max_length=64,unique=True)
    #昵称
    nickname = models.CharField(max_length=64,unique=False)
    #关注的城市
    city = models.TextField(default=[])
    #关注的股票
    stock = models.TextField(default=[])
    #关注的星座
    constellation = models.TextField(default=[])
from django.db import models


# Create your models here.
class User(models.Model):
    # openid
    openid = models.CharField(max_length=64, unique=True)
    # 昵称
    nickname = models.CharField(max_length=64, unique=False)
    # 关注的城市
    city = models.TextField(default=[])
    # 关注的股票
    stock = models.TextField(default=[])
    # 关注的星座
    constellation = models.TextField(default=[])
    # def __str__(self):
    #     return self.nickname
    class Meta:
        """
        Meta  元 描绘本身
        """
        # db_table = 'abc'  #重命名表名
        #添加索引
        indexes = [models.Index(fields=['nickname'],name='nickname')]


