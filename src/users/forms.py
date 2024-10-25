from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from captcha.fields import CaptchaField,CaptchaTextInput
from .models import Article,Favorite
CustomUser = get_user_model()

class RegisterForm(UserCreationForm):
    captcha = CaptchaField(widget=CaptchaTextInput())
    class Meta:
        model = CustomUser
        fields = ['username', 'email','password1', 'password2', 'avatar', 'bio']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','tags','picture']

class EmailLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    code = forms.CharField(max_length=8)
        

        