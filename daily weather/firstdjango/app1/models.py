from django.db import models

class Article(models.Model):
    #id
    article_id = models.AutoField(primary_key = True)
    #标题
    title = models.TextField()
    #摘要
    brief_content = models.TextField()
    #内容
    content = models.TextField()
    #日期
    publish_date = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title




