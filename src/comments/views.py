from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Comment
from users.models import Article
from notifications.views import post_notification
from .forms import CommentForm

# 发送邮件
@login_required
def post_comment(request,article_id):
    # 获取文章信息
    article = get_object_or_404(Article,id=article_id)
    if request.method == "POST":
        # 设置评论表单
        form = CommentForm(request.POST)
        if form.is_valid():
            # 暂存评论基本信息
            comment = form.save(commit=False)
            # 设置评论文章及作者 
            comment.article = article
            comment.user = request.user
            # 保存评论
            comment.save()
            if request.user != article.author:
                # 若评论者不是文章作者，则向作者发送通知
                post_notification(request,article_id,comment.id)
            # 返回文章详情页面
            return redirect(article)
        else:
            # 评论有误则给出提醒
            return HttpResponse("评论内容有误，清重新填写")
        
# 删除邮件
@login_required
def delete_comment(request,comment_id):
    # 获取评论信息
    comment = get_object_or_404(Comment,id=comment_id)
    # 获取评论相关文章
    article = comment.article
    if request.method == 'POST':
        # 删除评论
        comment.delete()  
    # 返回文章详情界面
    return    redirect(article)
    
    