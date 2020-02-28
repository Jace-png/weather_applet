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
