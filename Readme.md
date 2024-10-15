# 这是一份说明文档

本项目为openlab纳新题Easy Backend提供的辅助框架，便于大家更好的入门后端开发。

作为辅助性的框架，它当然没有完成所有的功能——我删去了大多数视图函数的逻辑，保留了models.py，urls.py，你需要对其进行完善或修改，使其能够满足验收要求。

（这应该是一道比较水的题目吧）

## 你要做的

在项目开始之前，请先认真学习（至少了解）一下Django和Python吧！推荐使用官方的入门文档进行学习：https://docs.djangoproject.com/zh-hans/5.1/intro/

你可以选择补全函数的逻辑，使其发挥原本的作用，或者根据自己的理解对模型、视图函数、url配置等进行修改，添加更多新的功能——请记住，辅助框架的作用仅仅是降低难度，我们不会对你的实现方式作任何限制。

那么，预祝大家学习愉快

## 项目结构

```
├── avatars
│   └── 屏幕截图_2022-09-15_233242.png      # 储存用户头像图片的文件夹
├── db.sqlite3                               # SQLite 数据库文件
├── manage.py                                 # Django 项目管理脚本
├── myproject                                 # 主项目文件夹
│   ├── __init__.py                           # 项目的初始化文件
│   ├── __pycache__                           # 编译后的 Python 文件缓存 
│   ├── asgi.py                               # ASGI 配置文件
│   ├── settings.py                           # 项目设置文件
│   ├── urls.py                               # 项目 URL 路由配置
│   └── wsgi.py                               # WSGI 配置文件
└── users                                      # 用户相关功能模块
    ├── __init__.py                           # 用户模块的初始化文件
    ├── __pycache__                           # 编译后的 Python 文件缓存
    ├── admin.py                               # Django 管理后台配置
    ├── apps.py                                # 应用配置
    ├── forms.py                               # 表单定义
    ├── migrations                             # 数据库迁移文件
    │                     
    ├── models.py                              # 数据模型定义
    ├── templates                              # 前端模板文件
    │   ├── article_detail.html               # 文章详情模板
    │   ├── article_list.html                 # 文章列表模板
    │   ├── create_article.html               # 创建文章模板
    │   ├── delete_article.html               # 删除文章模板
    │   ├── login.html                        # 登录模板
    │   ├── register.html                     # 注册模板
    │   ├── update_article.html               # 更新文章模板
    │   └── user_home.html                    # 用户主页模板
    ├── tests.py                               # 测试文件
    ├── urls.py                                # 用户模块 URL 路由配置
    └── views.py                               # 视图函数定义
```

## 项目功能

该 Django 项目主要实现以下功能：

1. **用户管理**
   - 用户注册
   - 用户登录
   - 用户主页展示

2. **文章管理**
   - 创建文章
   - 更新文章
   - 删除文章
   - 查看文章列表及详情

3. **模板系统**
   - 使用 Django 的模板引擎来渲染 HTML 页面

## 环境要求

- Python 3.10 或更高版本
- Django 4.x（根据需要可以自行选择版本）
- SQLite 数据库（默认）

## 安装与运行

1. **克隆项目**

   ```bash
   git clone <项目仓库链接>
   cd <项目文件夹>
   ```

2. **创建虚拟环境（可选）**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **安装依赖**

   创建一个 `requirements.txt` 文件并添加以下内容：

   ```
   Django>=4.0
   ```

   然后运行：

   ```bash
   pip install -r requirements.txt
   ```

4. **数据库迁移**

   运行以下命令来进行数据库迁移：

   ```bash
   python manage.py migrate
   ```

5. **创建超级用户**

   运行以下命令创建一个超级用户，以便访问管理后台：

   ```bash
   python manage.py createsuperuser
   ```

6. **运行开发服务器**

   启动开发服务器：

   ```bash
   python manage.py runserver
   ```

   然后在浏览器中访问 `http://127.0.0.1:8000/` 查看项目。

---

