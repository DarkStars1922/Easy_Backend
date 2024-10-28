# Easy_Backend

[toc]

## 基本说明

​        经过艰苦开发，本项目实现了一些基本的网站功能，实现了部分用户交互功能，如<strong><u>点赞，收藏，拉黑，评论，通知,并可以*取消相关操作*</u></strong>，如可以对<u>评论，通知和文章</u>进行**删除**操作，还可以**取消**<u>拉黑，点赞和收藏</u>；拥有**用户信箱**，可接收**各种通知**,并且对不同类型的通知可以进行**<u>分类查看</u>**；实现了**用户头像和文章图片的*上传*和*修改*操作**，且在更新后会**删除原文件**，节省存储空间；<u>**通过*redis*实现了对文章列表分页界面的缓存**</u>；可以通过**文章标题、内容的文本和相应标签**进行**模糊联合搜索**，且可通过点击标签进行对含有相同标签文章的精确搜索。并通过**.*gitignore*文件实现了对缓存文件，数据库文件和venv虚拟环境文件的忽略**;在用户主页可以看到自己的基本介绍、头像、文章、收藏夹、黑名单和信箱,此外，为防止个人文章过多影响页面效果，我们也<em>**对个人文章进行了<u>分页</u>**</em>,以提升用户体验。最后，将主页重定向为文章列表，以优化打开网站后的效果。

## 项目结构

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

## 项目功能

该 Django 项目主要实现以下功能：

1. **用户管理**
   - 用户注册(需要图形验证码)
   - 用户帐密登录
   - 用户邮箱验证码登录
   - 用户退出登录
   - 用户黑名单及取消拉黑
   - 用户注销
   - 用户主页展示(可随时更新头像,且对个人文章进行分页处理)


2. **文章管理**
   - 创建文章(含图片)
   - 更新文章(含图片)
   - 删除文章
   - 收藏文章及取消收藏
   - 查看缓存的文章列表
   - 查看文章详情和相关评论
3. **评论功能**
   - 发表评论
   - 删除评论
4. **通知功能**
   - 用户信箱
   - 推送通知(评论、点赞、收藏相关)
   - 通知分类
   - 通知已读确认
   - 清空信箱
5. **点赞功能**
   - 点赞文章及取消点赞
6. **模板系统**
   - 使用 Django 的模板引擎来渲染 HTML 页面



