from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, verbose_name='内容类型')
    object_id = models.PositiveIntegerField(verbose_name='对象ID')
    # 通过内容类型和ID定位内容对象
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField(verbose_name='内容')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='用户')

    class Meta:
        verbose_name = '评论库'
        verbose_name_plural = '评论库'
        ordering = ('-comment_time',)
