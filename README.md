# Easy_Backend

## 基本说明

经过艰苦开发，本项目实现了一些基本的网站功能，实现了部分用户交互功能，如点赞，收藏，拉黑，评论，通知；可以对评论，通知和文章进行删除操作；拥有用户信箱，可接收各种通知；
实现了用户头像和文章图片的上传和修改操作，且在更新后会删除原文件，节省存储空间；通过*redis*实现了对文章列表分页界面的缓存；可以通过文章标题、内容文本和标签进行模糊的
联合搜索，且可通过点击标签进行对含有相同标签文章的精确搜索。并通过.*gitignore*文件实现了对缓存文件，数据库文件和venv虚拟环境文件的忽略。


### 项目结构

```
├── res                                         # 静态文件
└── src                                         # 代码文件
  ├── media                                     # 储存内部图片的文件夹
  │  ├── avatars                                # 储存用户头像图片的文件夹
  │  └── article_picture                        # 储存文章图片的文件夹
  ├── manage.py                                 # Django 项目管理脚本
  ├── myproject                                 # 主项目文件夹
  │   ├── __init__.py                           # 项目的初始化文件
  │   ├── __pycache__                           # 编译后的 Python 文件缓存 
  │   ├── asgi.py                               # ASGI 配置文件
  │   ├── settings.py                           # 项目设置文件
  │   ├── urls.py                               # 项目 URL 路由配置
  │   └── wsgi.py                               # WSGI 配置文件
  ├── notifications                             # 通知相关功能模块
  |   ├── __init__.py                           # 通知模块的初始化文件
  |   ├── admin.py                              # Django 管理后台配置
  |   ├── apps.py                               # 应用配置
  |   ├── migrations                            # 数据库迁移文件
  |   ├── models.py                             # 数据模型定义
  |   ├── templates                             # 前端模板文件
  |   │   ├── mailbox.html                      # 用户信箱模板
  |   │   └── delete_notification.html          # 删除通知模板
  |   ├── tests.py                              # 测试文件
  |   ├── urls.py                               # 通知模块 URL 路由配置
  |   └── views.py                              # 视图函数定义
  ├── comments                                  # 评论相关功能模块
  |   ├── __init__.py                           # 评论模块的初始化文件
  |   ├── admin.py                              # Django 管理后台配置
  |   ├── apps.py                               # 应用配置
  |   ├── forms.py                              # 表单定义
  |   ├── migrations                            # 数据库迁移文件
  |   ├── models.py                             # 数据模型定义
  |   ├── tests.py                              # 测试文件
  |   ├── urls.py                               # 评论模块 URL 路由配置
  |   └── views.py                              # 视图函数定义
  ├── likes                                     # 点赞相关功能模块
  |   ├── __init__.py                           # 点赞模块的初始化文件
  |   ├── admin.py                              # Django 管理后台配置
  |   ├── apps.py                               # 应用配置
  |   ├── migrations                            # 数据库迁移文件
  |   ├── models.py                             # 数据模型定义
  |   ├── tests.py                              # 测试文件
  |   ├── urls.py                               # 点赞模块 URL 路由配置
  |   └── views.py                              # 视图函数定义
  └── users                                     # 用户相关功能模块
      ├── __init__.py                           # 用户模块的初始化文件
      ├── admin.py                              # Django 管理后台配置
      ├── apps.py                               # 应用配置
      ├── forms.py                              # 表单定义
      ├── migrations                            # 数据库迁移文件
      ├── models.py                             # 数据模型定义
      ├── email_sender.py                       # 生成验证码及发送邮件功能定义
      ├── templates                             # 前端模板文件
      │   ├── article_detail.html               # 文章详情模板
      │   ├── article_list.html                 # 文章列表模板
      │   ├── create_article.html               # 创建文章模板
      │   ├── delete_article.html               # 删除文章模板
      │   ├── login.html                        # 帐密登录模板
      │   ├── email_login.html                  # 邮箱登录模板
      │   ├── register.html                     # 注册模板
      │   ├── update_article.html               # 更新文章模板
      │   └── user_home.html                    # 用户主页模板
      ├── tests.py                              # 测试文件
      ├── urls.py                               # 用户模块 URL 路由配置
      └── views.py                              # 视图函数定义
```

### 项目功能

该 Django 项目主要实现以下功能：

1. **用户管理**
   - 用户注册
   - 用户登录
   - 用户退出登录
   - 用户注销
   - 用户主页展示

2. **文章管理**
   - 创建文章
   - 更新文章
   - 删除文章
   - 收藏文章
   - 查看文章列表及详情
    

2. **文章管理**
   - 创建文章
   - 更新文章
   - 删除文章
   - 收藏文章
   - 查看文章列表及详情
    

2. **文章管理**
   - 创建文章
   - 更新文章
   - 删除文章
   - 收藏文章
   - 查看文章列表及详情
    

2. **文章管理**
   - 创建文章
   - 更新文章
   - 删除文章
   - 收藏文章
   - 查看文章列表及详情
    

3. **模板系统**
   - 使用 Django 的模板引擎来渲染 HTML 页面



