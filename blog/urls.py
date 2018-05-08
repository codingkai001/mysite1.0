from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

# 定义命名空间，在模板中url编码中用 {% url '应用名:视图名' *args %}
app_name = 'blog'
urlpatterns = [
    # localhost:8000/article/

    path('', article_list, name='article_list'),
    path('<int:article_id>', article_detail, name='article_detail'),
    path('category/<str:label>', articles_with_type, name='articles_with_type'),
    path('date/<int:year>/<int:month>', articles_with_date, name='articles_with_date'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
