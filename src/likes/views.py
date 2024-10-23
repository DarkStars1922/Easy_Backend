from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from users.models import Article
from .models import Like

@login_required
def like(request,article_id):
    user = request.user
    article = Article.objects.get(id=article_id)
    like = Like.objects.create(user=user,article=article)
    like.save()
    article.like_count += 1
    article.save()
    return redirect(article)

@login_required
def unlike(request,article_id):
    user = request.user
    article = Article.objects.get(id=article_id)
    like = Like.objects.get(user=user,article=article)
    like.delete()
    article.like_count -= 1
    article.save()
    return redirect(article)
    


