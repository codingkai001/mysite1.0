from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from datetime import timedelta, datetime
from django.core.paginator import Paginator
from .models import Article, Category
from comment.models import Comment
from comment.forms import CommentForm


def article_detail(request, article_id):
    # 更新时last_update_time也会随着更新，需要改善
    article = get_object_or_404(Article, pk=article_id)

    # cookie失效时阅读量+1
    if not request.COOKIES.get('blog_%s_readed' % article_id):
        article.readed_nums += 1
        article.save()

    context = dict()
    article_content_type = ContentType.objects.get_for_model(article)
    comments = Comment.objects.filter(content_type=article_content_type, object_id=article.pk)
    context['comments'] = comments
    # 获取上一篇文章
    context['previous_article'] = Article.objects.filter(last_update_time__gt=article.last_update_time).last()
    # 获取下一篇文章
    context['next_article'] = Article.objects.filter(last_update_time__lt=article.last_update_time).first()
    context['article'] = article
    # print(article.category_set.all())
    context['labels'] = article.category_set.all()
    data = dict()
    data['content_type'] = article_content_type.model
    data['object_id'] = article_id
    context['comment_form'] = CommentForm(initial=data)
    response = render(request, 'blog/article_detail.html', context)
    response.set_cookie('blog_%s_readed' % article_id, 'true', expires=datetime.now()+timedelta(seconds=60))
    return response


def article_list(request):
    # 也可以用排除:Article.objects.exclude(is_published=False)， 与filter相反
    # articles = get_list_or_404(Article, is_published=True)
    articles = Article.objects.filter(is_published=True)
    # 将article每10个分一页
    paginator = Paginator(articles, 10)
    # 获取url中的页码参数
    page_num = request.GET.get('page', 1)   # 默认返回第一页
    articles_of_the_page = paginator.get_page(page_num)      # 获取某一页的articles，不合法的参数将默认返回第一页
    context = dict()
    label_count = []        # 博客分类及计数
    labels = Category.objects.values('type_name').distinct()
    for label in labels:
        # label是Category对象的字段形成的字典
        count = Category.objects.filter(type_name=label['type_name']).count()
        label['count'] = count
        label_count.append(label)
    context['all_labels'] = label_count
    context['articles'] = articles_of_the_page
    context['article_count'] = articles.count()
    # 得到按月份分类的时间列表
    context['articles_date'] = Article.objects.dates('last_update_time', 'month', 'DESC')
    return render(request, 'blog/article_list.html', context)


def articles_with_type(request, label):
    context = dict()
    label_objs = Category.objects.filter(type_name=label)
    # articles = label_objs.values('article').order_by('-last_update_time')
    articles = []
    for article in label_objs:
        articles.append(article)
    paginator = Paginator(articles, 10)
    page_num = request.GET.get('page', 1)  # 默认返回第一页
    articles_of_the_page = paginator.get_page(page_num)
    context['label'] = label
    context['articles'] = articles_of_the_page
    context['count'] = label_objs.count()
    return render_to_response('blog/articles_with_type.html', context)


def articles_with_date(request, year, month):
    # print(year, month)
    articles = Article.objects.filter(last_update_time__year=year, last_update_time__month=month).all()
    print(articles)
    # 将article每10个分一页
    paginator = Paginator(articles, 10)
    # 获取url中的页码参数
    page_num = request.GET.get('page', 1)
    page_of_articles = paginator.get_page(page_num)  # 不合法的参数将默认返回第一页
    print(page_of_articles)
    context = dict()
    label_count = []  # 博客分类及计数
    labels = Category.objects.values('type_name').distinct()
    for label in labels:
        # label是Category对象的字段形成的字典
        count = Category.objects.filter(type_name=label['type_name']).count()
        label['count'] = count
        label_count.append(label)
    context['all_labels'] = label_count
    context['date'] = '%s年%s月' % (year, month)
    context['articles'] = page_of_articles
    context['article_count'] = articles.count()
    # 得到按月份分类的时间列表
    context['articles_date'] = Article.objects.dates('last_update_time', 'month', 'DESC')
    return render_to_response('blog/articles_with_date.html', context)
