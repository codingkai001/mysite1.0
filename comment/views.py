from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import Comment
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from .forms import CommentForm


def update_comment(request):
    # # 后期异常处理与优化
    # user = request.user
    # text = request.POST.get('text', '')
    # content_type = request.POST.get('content_type', '')
    # object_id = int(request.POST.get('object_id', ''))
    # # 获取对象模型
    # model_class = ContentType.objects.get(model=content_type).model_class()
    # model_obj = model_class.objects.get(pk=object_id)
    #
    # comment = Comment()
    # comment.user = user
    # comment.text = text
    # comment.content_object = model_obj
    # comment.save()
    #
    # referer = request.META.get('HTTP_REFERER', reverse('home'))
    # return HttpResponseRedirect(referer)

    referer = request.META.get('HTTP_REFERER', reverse('home'))
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = Comment()
        # comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.user = request.user
        comment.content_object = comment_form.cleaned_data['content_object']
        comment.save()
        data = dict()
        return HttpResponseRedirect(referer)
    else:
        return HttpResponse('评论出错')

