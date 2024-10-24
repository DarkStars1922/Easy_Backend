from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Article,Favorite
CustomUser = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password1','password2','bio']
        # fields = ['username', 'password1', 'password2', 'avatar', 'bio']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']
        