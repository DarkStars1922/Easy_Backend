from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from users.models import Article
from notifications.views import post_notification
from .forms import CommentForm

@login_required
def post_comment(request,article_id):
    article = get_object_or_404(Article,id=article_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            if request.user != article.author:
                post_notification(request,article_id)
            return redirect(article)
        else:
            return HttpResponse("评论内容有误，清重新填写")
