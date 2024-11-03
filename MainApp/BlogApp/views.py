from django .contrib.auth import login , logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.urls import reverse
from .forms import RegisterForm
from .forms import PostForm
from .models import Post, Tag, Category
import re

# Create your views here.

def home(request):
    return render (request, "BlogApp/intro.html")


def user_login(request):
    form = RegisterForm()
    if request.method == 'POST':
        form_type = request.POST.get("form_type")

        if form_type == "login":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Login successful! welcome {username}')
                print(messages.get_messages(request))
                return redirect('feed')
            else:
                # Handle invalid login
                messages.error(request,"Invalid username or password.") 
                return render(request, 'registration/login.html')

        elif form_type == "Register":
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                messages.success(request, f'welcome {username}, you have successfully registered! You can now login')
                form.save()
                 
           
               

   
    
    return render(request, 'registration/login.html', {'form': form})

    

@login_required (login_url ='login')
def feed(request):
    post = Post.objects.all()
    categories = Category.objects.all()
    return render(request,'BlogApp/feed.html', {
        'post': post,
        'categories': categories
        })

@login_required (login_url ='login')
def create_post(request):
    form = PostForm()
    if request.method == "POST":
        
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save() 
            description = form.cleaned_data['description']
            hashtags = re.findall(r'#(\w+)', description)
            for tag_name in hashtags:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)   
            selected_categories = form.cleaned_data['Category']
            post.Category.set(selected_categories)
            messages.success(request, "Post created successfully")
            return redirect ('feed')
        else:
            messages.error (request,"Post creation was unsuccessful. Please check the form.")


    return render(request,"BlogApp/create_post.html", {"form": form})

def user_logout(request):
    logout(request)
    messages.success(request,'Logout Successful!')
    return redirect(reverse('login'))