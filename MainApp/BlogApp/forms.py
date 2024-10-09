from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Post, Tag, Category


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    Dp = forms.ImageField()


    class Meta :
        model = User 
        fields = ["username", "email","Dp", "password1", "password2"]

class PostForm(forms.ModelForm):

    class Meta:
        model =Post
        fields = [ "description"]