from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm,ArticleCreateForm
from .models import CustomUser, Article, Favorite
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

# 用户注册
def register(request):
    # 检查请求方法是否为 POST
    if request.method == 'POST':
        # 创建表单实例，传入 POST 数据和文件
        form = RegisterForm(request.POST)
        #form = RegisterForm(request.POST, request.FILES)
        # 验证表单数据是否有效
        if form.is_valid():
            #检验两次输入密码是否一致
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                raise forms.ValidationError("两次密码输入不一致，请重试")
            # 保存用户数据并创建用户实例
            user = form.save()
            # 自动登录新注册的用户
            login(request, user)
            # 重定向到用户主页，其中'user_home'对应urls.py中的path('home/', views.user_home, name='user_home'),可以根据需要修改重定向的 URL
            return redirect('user_home')
    else:
        # 如果不是 POST 请求，则创建一个空的表单实例
        form = RegisterForm()
    
    # 渲染注册页面，并传递表单上下文
    return render(request, 'register.html', {'form': form})


# 用户登录
def user_login(request):
    
    if request.method == 'POST':
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
            return redirect('user_home')
        except:
            #对于失败的查询，给出警告信息
            message = '用户名或密码错误'
            return HttpResponse('用户名或密码错误')
    else:
        form = LoginForm()
    # return render(request, 'login.html', {'form': form})
    return render(request,'login.html',{'form':form})

# 用户登出
def user_logout(request):
    #清除当前会话数据，达到登出效果
    logout(request)
    return redirect('login')


# 注销账户
@login_required
def delete_account(request):
        #获取用户
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
    article = Article.objects.get(article_id=article_id)
    if request.method == "POST":
        article_form = ArticleCreateForm(request.POST)
        title = article_form.cleaned_data['title']
        content = article_form.cleaned_data['content']
        article.title = title
        article.content = content
        article.save()
    else:
        article_form = ArticleCreateForm()
    # return render(request, 'update_article.html', {'article': article})
    return render(request,'update_article.html',{'article': article})

# 删除文章
@login_required
def delete_article(request, article_id):
    article = Article.objects.get(article_id=article_id)
    article.delete()
    return redirect('user_home')

# 用户主页
@login_required
def user_home(request):
    

    return render(request, 'user_home.html', {
        # 'user': ,
        # 'articles': ,
        # 'favorite_articles': 
    })

# 收藏文章
@login_required
def favorite_article(request, article_id):
    
    return redirect('user_home')

# 文章列表视图
def article_list(request):

    # return render(request, 'article_list.html', {'page_obj': page_obj})
    return

# 文章详情视图
@login_required
def article_detail(request, article_id):

    return render(request, 'article_detail.html', {
        # 'article': ,
        # 'is_favorited': 
    })
