from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    content = RichTextUploadingField(verbose_name='正文')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # 新增文章时自动添加当前时间
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='发表时间')  # 更新时自动修改为当前时间
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1, verbose_name='作者')
    # 关联User表， 不与User级联，默认为root(id=1)
    # 后期修改，存为草稿或者立即发表
    is_published = models.BooleanField(default=False, verbose_name='是否发表')   # 是否已发表
    readed_nums = models.IntegerField(default=0, verbose_name='浏览量')    # 阅读量
    # article_type = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    # article_type = models.ManyToManyField(Category, related_name='related_articles', verbose_name='标签')

    # 默认返回该对象的title
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_update_time', ]
        verbose_name = '文章列表'
        verbose_name_plural = '文章列表'


class Category(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, verbose_name='文章', null=True)
    type_name = models.CharField(max_length=30, verbose_name='标签名称')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '标签组'
        verbose_name_plural = '标签组'






