from django.contrib import admin
from .models import Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'readed_nums', 'is_published', 'created_time', 'last_update_time')  # 多对多字段不能显示
    ordering = ('-id',)      # 逆序排序


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'type_name')


admin.site.site_header = '博客后台管理系统'
admin.site.site_title = '博客'


