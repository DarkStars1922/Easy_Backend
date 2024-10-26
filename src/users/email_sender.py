from django.shortcuts import render
from random import Random
from django.core.mail import send_mail
from django.conf import settings

# 生成随机验证码
def random_code(randomlength):
    code = ''
    string = '0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    string_len = len(string) - 1
    for i in range(randomlength):
        # 获取基本字符串的相应字符存入验证码
        code += string[Random().randint(0,string_len)] 
    return code

# 发送验证码邮件
def send_code_email(email):
    # 生成验证码
    code = random_code(8)
    # 初始化邮件信息
    email_title = "用户登录"
    email_body = "您的邮箱验证码为:{0},请利用该验证码登录帐号".format(code)
    # 发送邮件
    send_mail(email_title,email_body,settings.EMAIL_FROM,[email])
    return code
        