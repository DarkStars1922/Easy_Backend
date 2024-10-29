from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import Favorite
from comments.models import Comment
from likes.models import Like
from .models import Notification

# 用户信箱
@login_required
def mailbox(request):
    # 获取当前用户相关所有通知
    tag = request.GET.get('tag')
    notifications = Notification.objects.filter(receiver=request.user)
    if tag:
        notifications = notifications.filter(tag=tag)
    # 返回邮箱界面
    return render(request,'mailbox.html',{'notifications':notifications,'tag':tag})

# 发送通知
@login_required
def post_notification(request):
    # 通过获取id，判断通知类型
    comment_id = request.session.get("comment")
    favorite_id = request.session.get("favorite")
    like_id = request.session.get("like")
    # 获取通知相关发送对象
    sender = request.user
    # 创建一条通知
    if comment_id:
        # 评论相关
        comment = get_object_or_404(Comment,id=comment_id) 
        article = comment.article
        receiver = article.author 
        Notification.objects.create(sender=sender,article=article,receiver=receiver,content="评价了你的",comment=comment,tag='comment')
    elif like_id:
        # 点赞相关
        like = get_object_or_404(Like,id=like_id) 
        article = like.article
        receiver = article.author 
        Notification.objects.create(sender=sender,article=article,receiver=receiver,content="点赞了你的",like=like,tag='like')
    elif favorite_id:
        # 收藏相关
        favorite = get_object_or_404(Favorite,id=favorite_id) 
        article = favorite.article
        receiver = article.author 
        Notification.objects.create(sender=sender,article=article,receiver=receiver,content="收藏了你的",favorite=favorite,tag='favorite')
        
    
# 标记已读
@login_required
def mark_as_read(request,notification_id):
    # 获取当前通知
    notification = Notification.objects.get(id=notification_id)
    # 设置已读取并保存通知阅读情况
    notification.read = True
    notification.save()
    # 回到信箱
    return redirect('notifications:user_mailbox')    

# 删除通知
@login_required
def delete_notification(request,notification_id):
    # 获取待删除通知
    notification = Notification.objects.get(id=notification_id)
    if request.method == 'POST':
        # 删除该通知
        notification.delete()
        # 删除后返回信箱
        return  redirect('notifications:user_mailbox')
    # 进入二次确认界面
    return render(request,'delete_notification.html')

# 清空邮箱
@login_required
def clean_mailbox(request):
    if request.method=="POST":
        # 获取和信箱主人相关的所有通知
        notifications = Notification.objects.filter(receiver=request.user)
        for notification in notifications:
            # 删除每条通知
            notification.delete()
    # 返回信箱
    return redirect("notifications:user_mailbox")