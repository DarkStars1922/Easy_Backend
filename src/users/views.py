
from django.shortcuts import render, redirect,reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from pure_pagination import Paginator as P
from comments.models import Comment
from notifications.models import Notification
from likes.models import Like
from notifications.views import post_notification
from .forms import RegisterForm, LoginForm, ArticleCreateForm
from .models import CustomUser, Article, Favorite,Blacklist
from .email_sender import send_code_email
import collections
collections.Iterable = collections.abc.Iterable



# 用户注册
def register(request):
    # 检查请求方法是否为 POST
    if request.method == 'POST':
        # 创建表单实例，传入 POST 数据和文件
        form = RegisterForm(request.POST, request.FILES)
        # 验证表单数据是否有效
        if form.is_valid():
            username = form.cleaned_data['username']
            if CustomUser.objects.filter(username=username):
                return HttpResponse("当前用户名已被注册")
            # 检验两次输入密码是否一致
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                raise HttpResponse("两次密码输入不一致，请重试")
            # 保存用户数据并创建用户实例
            user = form.save()
            # 重定向到用户主页并设置COOKIE
            login(request,user)
            response =  redirect('user_home')
            response.set_cookie('username',username,300)
            return response
    else:
        # 如果不是 POST 请求，则创建一个空的表单实例
        form = RegisterForm()
    # 渲染注册页面，并传递表单上下文
    return render(request, 'register.html', {'form': form})


# 用户帐密登录
def user_login(request):
    message=''
    if request.method == 'POST':
        # 防止重复登录
        if request.COOKIES.get('username'):
            return redirect("user_home")
        form = LoginForm(request.POST)
        if form.is_valid():
            # 获取用户名和密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        try:
            # 查找是否存在符合的用户
            user = authenticate(username=username,password=password)
            # 登录已存在的用户并设置COOKIE
            login(request,user)
            response =  redirect('user_home')
            response.set_cookie('username',username,300)
            return response
        except:
            # 对于失败的查询，给出警告信息
            message='用户名或密码错误'
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form,'message':message})

# 用户邮箱登录
def email_login(request):
    # 初始化按钮和警告信息
    message = ''
    button = "获取验证码"
    if request.method == 'POST':
        # 获取邮件和验证码信息，并初始化验证码情况
        email = request.POST.get('email')
        code = request.POST.get('code',)
        have_code = False
        # 获取邮件相关用户
        user = CustomUser.objects.filter(email=email)
        # 判断用户是否存在
        if  not user:
            # 不存在则返回警告信息
            message = "用户不存在"
        else:
            # 判断是否已经发送验证码
            if not request.session.get('saved_code'):
                # 未发送则重新初始化按钮，警告信息，并将验证码情况设置为存在
                button = "登录"
                message = "验证码已发送"
                have_code = True
                # 对获取到的邮箱发送验证码邮件
                saved_code = send_code_email(email)
                # 向请求的session中写入验证码
                request.session['saved_code'] = saved_code
            elif code == request.session.get('saved_code'):
                # 已经发送验证码且验证码正确则删除验证码信息
                del request.session['saved_code']
                # 获取邮箱相关联用户
                user = CustomUser.objects.get(email=email)
                # 登录用户并设置COOKIE
                login(request,user)
                response =  redirect('user_home')
                response.set_cookie('username',user.username,300)
                return response
            else:
                # 已经发送验证码但验证码错误则给出警告
                message = "验证码错误，请重试"
                # 重新设置验证码情况
                have_code = False
                # 删除现在的验证码信息
                del request.session['saved_code']
    # 渲染界面并映射本地信息
    return render(request,'email_login.html',locals())

# 用户登出
def user_logout(request):
    #清除当前Cookie，达到登出效果
    response = redirect('login')
    response.delete_cookie('username')
    logout(request)
    return response

# 注销账户
def delete_account(request):
        # 尝试获取Cookie
        username = request.COOKIES.get('username')
        # 未登录则跳转至登录界面
        if not username:
            return redirect('login')
        user = request.user
        # 删除用户
        user.delete()
        # 返回登录界面
        return redirect('login')
    
# 创建文章
@login_required
def create_article(request):
    # 检查请求方法
    if request.method == "POST":
        # 传入文章表单相关数据
        article_form = ArticleCreateForm(request.POST,request.FILES)
        # 验证文章表单是否合法
        if article_form.is_valid():
            # 保存文章，图片和作者
            article = article_form.save(commit=False)
            article.author = request.user
            article.save()
            # 保存文章标签
            article_form.save_m2m()
            # 返回主页
            return redirect('user_home')
    return render(request, 'create_article.html')
 
# 修改文章
@login_required
def update_article(request, article_id):
    # 获取待修改文章
    article = get_object_or_404(Article,id=article_id)
    # 判断修改用户是否为作者
    if request.user != article.author:
        # 修改用户不为作者则阻止编辑
        return HttpResponse("您无权编辑该文章")
    if request.method == "POST":
        # 获取修改信息
        title = request.POST['title']
        content = request.POST['content']
        picture = request.FILES['picture']
        # 进行修改
        article.title = title
        article.content = content
        # 删除原有图片文件
        article.delete_picture()
        # 为文章添加新图片
        article.picture = picture
        # 保存修改后文章
        article.save()
    else:
        article_form = ArticleCreateForm()
    return render(request,'update_article.html',{'article': article})

# 删除文章
@login_required
def delete_article(request, article_id):
    # 数据库获取目标文章
    article = get_object_or_404(Article,id=article_id)
    if request.method == 'POST':
        # 删除文章
        article.delete_picture()
        article.delete()
        # 返回主页
        return redirect('user_home')
    return render(request,'delete_article.html',{'article':article})

# 收藏文章
@login_required
def favorite_article(request, article_id):
    if request.method == "POST":
        # 获取收藏用户和文章
        user = request.user
        article = get_object_or_404(Article,id=article_id)
        # 判断用户是否收藏该文章
        favorite = Favorite.objects.filter(user=user,article=article)
        if not favorite:
            # 如果尚未收藏，创造收藏夹
            favorite = Favorite.objects.create(
               user = user,
                article = article
            )
            # 文章收藏数增加
            article.favorite_count += 1
            # 保存文章和收藏夹
            article.save()
            favorite.save()
            if user != article.author:
                # 若收藏者不为作者，将收藏夹id写入session
                request.session['favorite'] = favorite.id
                # 发送通知
                post_notification(request)
                # 删除收藏相关session，防止影响其他通知情况
                del request.session['favorite']
            # 返回收藏结果
            is_favorited = True
        else:
            # 如果已经收藏，取消收藏，文章收藏数减少
            article.favorite_count -= 1
            article.save()
            # 删除当前收藏夹对象
            favorite.delete()
            # 返回收藏结果
            is_favorited = False
    return render(request,'article_detail.html',{
        'article': article ,
        'is_favorited': is_favorited
    })
    
# 创建黑名单
@login_required
def create_blacklist(request,comment_id):
    # 获取评论对象
    comment = Comment.objects.get(pk=comment_id)
    # 获取评论所属的文章
    article = comment.article
    if request.method == "POST":
        # 获取用户和评论作者
        user = request.user
        blocker = comment.user
        # 创建并保存该黑名单
        blacklist = Blacklist.objects.create(
            user =user,
            blocker = blocker
        )
        blacklist.save()
        # 返回文章详情界面
        return  redirect(article)
            
# 移除黑名单            
@login_required
def delete_blacklist(request,blacklist_id):
    if request.method == 'POST':
        # 获取黑名单对象
        blacklist = Blacklist.objects.get(id=blacklist_id)
        # 删除黑名单
        blacklist.delete()
        # 返回主页
        return redirect('user_home')

# 用户主页 
def user_home(request):
    # 尝试获取Cookie
    username = request.COOKIES.get('username')
    # 未登录则跳转至登录界面
    if not username:
        return redirect('login')
    # 获取用户
    user = request.user
    # 尝试获取当前文章页数
    try:
        page = request.GET.get('page')
    except:
        page = 1
    # 如果不存在，设置为第一页
    if not page:
        page = 1
    # 监测用户是否修改头像
    if request.method == "POST":
        # 修改头像前删除原头像
        user.delete_avatar()
        # 获取新头像并保存
        avatar = request.FILES.get('avatar')
        user.avatar = avatar
        # 保存用户
        user.save()
    # 获取用户文章，收藏夹，未读邮件和黑名单
    articles = Article.objects.filter(author=user)
    favorite_articles = Favorite.objects.filter(user=user) 
    not_read_notifications = Notification.objects.filter(receiver=user,read=False)
    blacklists = Blacklist.objects.filter(user=user)
    # 对用户文章进行分页处理
    article_list = P(articles,3,request=request)
    article_page = article_list.page(page)
    return render(request, 'user_home.html', {
        'user': user,
        'article_page': article_page,
        'favorite_articles': favorite_articles ,
        'blacklists':blacklists,
        'not_read_notifications':not_read_notifications,
        'articles':articles,
    })

# 文章列表视图
def article_list(request):
    # 若Cookie信息过期，清空session用户相关内容
    if not request.COOKIES.get('username'):
        logout(request)
    # 获取搜索信息
    search = request.GET.get('search')
    search_tag = request.GET.get('search_tag')
    tag = request.GET.get('tag')
    
    # 取出所有文章
    article_list = Article.objects.all()
    
    if search:
        # 若文本搜索信息存在，则进行对文章标题和内容的综合模糊搜索
        article_list = article_list.filter(
            Q(title__icontains=search)|
            Q(content__icontains=search)
        ).distinct()
    else:
        # 若不存在，则将文本搜索设置为空
        search = ''
    
    # 若标签信息信息存在且不为空
    if tag and tag !='None':
        # 精确获取存在标签信息的文章
        article_list = article_list.filter(tags__name__in=[tag]).distinct()
    else:
        # 若不存在，则将标签信息设置为空
        tag = None
    if search_tag and search_tag !='None':
        # 若标签搜索信息存在且不为空，则进行对标签名的模糊搜索
        article_list = article_list.filter(tags__name__icontains=search_tag).distinct()
    else:
        # 若不存在，则将标签搜索设置为空
        search_tag=''
    # 进行分页操作
    paginator = Paginator(article_list,4)
    # 提取每一页
    page = request.GET.get('page')
    # 对联合搜索的页面设置缓存需要的键
    page_key="{0}{1}{2}_page_{3}".format(search,search_tag,tag,page)
    # 尝试获取缓存中该页信息
    cache_page=cache.get(page_key)
    if cache_page:
        # 缓存存在则直接获取
        page_obj = cache_page
    else:
        # 缓存不存在则重新设置缓存
        try:
            # 获取当前页面
            page_obj = paginator.get_page(page)
            # 缓存当前页面
            cache.set(page_key,page_obj,60)
        except:
            #若初始为空，主动跳转到第一页
            page_obj = paginator.get_page(1)
            # 缓存当前页面
            cache.set(page_key,page_obj,60)
    # 渲染页面并存入本地信息
    return render(request, 'article_list.html', {
        'page_obj': page_obj,
        'search':search,
        'tag':tag,
        'search_tag':search_tag,
        })

# 文章详情视图
def article_detail(request, article_id):
    # 尝试获取Cookie
    username = request.COOKIES.get('username')
    # 未登录则跳转至登录界面
    if not username:
        return redirect('login')
    if request.method == "POST":
        # 启用文章收藏
        favorite_article(request,article_id)
    # 初始化收藏，能否评论，点赞情况
    is_favorited = False
    comment_permission = True
    is_liked = False
    # 获取用户
    user = request.user
    # 获取相应文章
    article = get_object_or_404(Article,id = article_id)
    # 获取文章相关评论
    comments = Comment.objects.filter(article=article)
    # 判断当前用户是否已收藏该文章
    if Favorite.objects.filter(user=user,article=article):
        is_favorited = True
    # 判断当前用户是否被文章作者列入黑名单
    if Blacklist.objects.filter(blocker=user,user=article.author):
        comment_permission = False
    # 判断当前用户是否已点赞该文章
    if Like.objects.filter(user=user,article=article):
        is_liked=True
    # 传递信息并渲染页面
    return render(request, 'article_detail.html', {
        'article': article ,
        'is_favorited': is_favorited ,
        'comments': comments ,
        'comment_permission':comment_permission,
        'is_liked':is_liked
    })
