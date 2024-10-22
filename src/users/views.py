from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm, ArticleCreateForm
from .models import CustomUser, Article, Favorite
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from comments.models import Comment
from django.db.models import Q

# 用户注册
def register(request):
    # 检查请求方法是否为 POST
    if request.method == 'POST':
        # 创建表单实例，传入 POST 数据和文件
        form = RegisterForm(request.POST)
        #form = RegisterForm(request.POST, request.FILES)
        # 验证表单数据是否有效
        if form.is_valid():
            username = form.cleaned_data['username']
            if CustomUser.objects.filter(username=username):
                return forms.ValidationError("当前用户名已被注册")
            #检验两次输入密码是否一致
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                raise forms.ValidationError("两次密码输入不一致，请重试")
            # 保存用户数据并创建用户实例
            user = form.save()
            # 重定向到用户主页
            login(requesr,user)
            response =  redirect('user_home')
            response.set_cookie('username',username,300)
            return response
    else:
        # 如果不是 POST 请求，则创建一个空的表单实例
        form = RegisterForm()
    
    # 渲染注册页面，并传递表单上下文
    return render(request, 'register.html', {'form': form})


# 用户登录
def user_login(request):
    if request.method == 'POST':
        # 防止重复登录
        if request.COOKIES.get('username'):
            return redirect("user_home")
        form = LoginForm(request.POST)
        if form.is_valid():
            #获取用户名和密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        try:
            #查找是否存在符合的用户
            user = authenticate(username=username,password=password)
            #登录已存在的用户
            login(request,user)
            response =  redirect('user_home')
            response.set_cookie('username',username,300)
            return response
        except:
            #对于失败的查询，给出警告信息
            return forms.ValidationError('用户名或密码错误')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

# 用户登出
def user_logout(request):
    logout(request)
    #清除当前Cookie，达到登出效果
    response = redirect('login')
    response.delete_cookie('username')
    return response

# 注销账户
def delete_account(request):
        # 尝试获取Cookie
        username = request.COOKIES.get('username')
        # 未登录则跳转至登录界面
        if not username:
            return redirect('login')
        user = request.user
        #删除账户
        user.delete()
        return redirect('login')
    
# 创建文章
@login_required
def create_article(request):
    #检查请求方法
    if request.method == "POST":
        #传入文章表单相关数据
        article_form = ArticleCreateForm(request.POST)
        #验证文章表单是否合法
        if article_form.is_valid():
            #保存数据，回到主页
            article = article_form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('user_home')
    return render(request, 'create_article.html')
 
# 修改文章
@login_required
def update_article(request, article_id):
    # 获取待修改文章
    article = get_object_or_404(Article,id=article_id)
    # 判断修改用户是否为作者
    if request.user != article.author:
        return HttpResponse("您无权编辑该文章")
    if request.method == "POST":
        # 获取修改信息
        title = request.POST['title']
        content = request.POST['content']
        # 进行修改
        article.title = title
        article.content = content
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
        article.delete()
        # 返回主页
        return redirect('user_home')
    return render(request,'delete_article.html',{'article':article})

# 用户主页 
def user_home(request):
    # 尝试获取Cookie
    username = request.COOKIES.get('username')
    # 未登录则跳转至登录界面
    if not username:
        return redirect('login')
    # 获取用户
    user = request.user
    # 获取用户文章和收藏夹
    articles = Article.objects.filter(author=user)
    favorite_articles = Favorite.objects.filter(user=user) 
    return render(request, 'user_home.html', {
        'user': user,
        'articles': articles,
        'favorite_articles': favorite_articles 
    })

# 收藏文章
@login_required
def favorite_article(request, article_id):
    if request.method == "POST":
        # 获取收藏用户和文章
        user = request.user
        article = get_object_or_404(Article,id=article_id)
        # 创造收藏对象
        favorite = Favorite.objects.create(
            user = user,
            article = article
        )
        favorite.save()
        # 返回收藏结果
        is_favorited = True
    return render(request,'article_detail.html',{
        'article': article ,
        'is_favorited': is_favorited
    })

# 文章列表视图
def article_list(request):
    search = request.GET.get('search')
    if search:
        article_list = Article.objects.filter(
            Q(title_icontains=search)|
            Q(content_icontains=search)
        )
    else:
        search = ''
        # 取出所有文章
        article_list = Article.objects.all()
    # 进行分页操作
    paginator = Paginator(article_list,4)
    # 提取每一页
    page = request.GET.get('page')
    try:
        # 获取当前页面
        page_obj = paginator.get_page(page)
    except:
        #若初始为空，主动跳转到第一页
        page_obj = paginator.get_page(1)
    return render(request, 'article_list.html', {'page_obj': page_obj,'search':search})

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
    # 取出相应文章
    is_favorited = False
    user = request.user
    article = get_object_or_404(Article,id = article_id)
    comments = Comment.objects.filter(article=article)
    # 判断是否已被当前用户收藏
    if Favorite.objects.filter(user=user,article=article):
        is_favorited = True
    # 传递对象并渲染页面
    return render(request, 'article_detail.html', {
        'article': article ,
        'is_favorited': is_favorited ,
        'comments': comments
    })
