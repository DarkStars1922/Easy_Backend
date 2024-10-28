from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from users.models import Article
from notifications.views import post_notification
from .models import Like

# 点赞功能
@login_required
def like(request,article_id):
     # 获取相关的用户与文章
    user = request.user
    article = Article.objects.get(id=article_id)
    # 创建赞并保存点赞情况
    like = Like.objects.create(user=user,article=article)
    like.save()
    if user != article.author:
        request.session['like'] = like.id
        post_notification(request)
        del request.session['like']
    # 增加文章点赞数并保存
    article.like_count += 1
    article.save()
    # 返回文章详情界面
    return redirect(article)

# 取消点赞
@login_required
def unlike(request,article_id):
    # 获取相关的用户与文章
    user = request.user
    article = Article.objects.get(id=article_id)
    # 获取赞的信息
    like = Like.objects.get(user=user,article=article)
    # 删除赞
    like.delete()
    # 减少文章点赞数并保存
    article.like_count -= 1
    article.save()
    # 返回文章详情页面
    return redirect(article)
    


