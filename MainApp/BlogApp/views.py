from django .contrib.auth import login , logout, authenticate
from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form_type = request.POST.get("form_type")

        if form_type == "login":
            # Retrieve username and password from the request
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Login the user if authentication was successful
                login(request, user)
                messages.success(request, f'Login successful! welcome {username}')
                return redirect('feed')
            else:
                # Handle invalid login
                error_message = "Invalid username or password."
                return render(request, 'registration/login.html', {'error_message': error_message})

        elif form_type == "Register":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = user.username
                messages.success(request, f'welcome {username}, you have successfully registered!')
                login(request, user)  
                return redirect('feed')
            else:
                form = RegisterForm()
                messages.error(request, 'There was an error with your registration. Please try again.')
               

    else:
        form = RegisterForm()
    return render(request, 'registration/login.html', {'form': form})

    


def feed(request):
    post = Post.objects.all()
    categories = Category.objects.all()
    return render(request,'BlogApp/feed.html', {
        'post': post,
        'categories': categories
        })


def create_post(request):
    if request.method == "POST":
        
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save() 
            # Extracting tag's from the description
            description = form.cleaned_data['description']
            hashtags = re.findall(r'#(\w+)', description)
            # Adding the tags
            for tag_name in hashtags:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)
            #saving the categories    
            selected_categories = form.cleaned_data['Category']
            post.Category.set(selected_categories)
            print ("Post saved successfully")
            return redirect ('feed')
        else:
            print("unseccessfull")

    else:
        form = PostForm()
    return render(request,"BlogApp/create_post.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect(reverse('login'))