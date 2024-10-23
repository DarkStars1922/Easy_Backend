from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import Article
from comments.models import Comment
from .models import Notification

@login_required
def mailbox(request):
    notifications = Notification.objects.filter(receiver=request.user)
    return render(request,'mailbox.html',{'notifications':notifications})

@login_required
def post_notification(request,article_id,comment_id):
    sender = request.user
    article = get_object_or_404(Article,id=article_id)
    comment = get_object_or_404(Comment,id=comment_id)
    receiver = article.author
    Notification.objects.create(sender=sender,article=article,receiver=receiver,content="评价了你的",comment=comment)
    
@login_required
def mark_as_read(request,notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.read = True
    notification.save()
    return redirect('notifications:user_mailbox')    