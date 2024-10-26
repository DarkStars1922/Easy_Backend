"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import article_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',article_list,name='homepage'), # 主页的URL
    path('users/', include('users.urls')),  # 包含用户应用的URL
    path('comments/',include('comments.urls')), # 包含评论应用的URL
    path('notifications/',include('notifications.urls')), # 包含通知应用的URL
    path('likes/',include('likes.urls')), # 包含点赞应用的URL
    path('capcha',include('captcha.urls')) # 包含图形验证码应用的URL
]

# 添加内部静态文件地址
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
