from django.shortcuts import render
from random import Random
from django.core.mail import send_mail
from django.conf import settings
def random_code(randomlength):
    code = ''
    string = '0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    string_len = len(string) - 1
    for i in range(randomlength):
        code += string[Random().randint(0,string_len)] 
    return code

def send_code_email(email):
    code = random_code(8)
    email_title = "用户登录"
    email_body = "您的邮箱验证码为:{0},请利用该验证码登录帐号".format(code)
    send_mail(email_title,email_body,settings.EMAIL_FROM,[email])
    return code
        