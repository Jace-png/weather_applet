from django.contrib import admin

# Register your models here.
from .models import Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','brief_content','content','publish_date']
admin.site.register(Article,ArticleAdmin)  #注册模型
