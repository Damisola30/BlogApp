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

        elif form_type == "sign_up":
            username = request.POST.get('username')
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)  # Log the user in after registration
                messages.success(request, f'welcome {username}, you have successfully registered!')
                return redirect(reverse('feed'))
            else:
                print("error")
                # Handle form errors during registration
                return render(request, 'registration/login.html', {'form': form,})

    else:
        form = RegisterForm()  # Initialize an empty form for registration

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
        print ("form submitted successfully")
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

             # Extract words starting with # from the description
            description = form.cleaned_data['description']
            hashtags = re.findall(r'#(\w+)', description)

            # Add the extracted tags to the post
            for tag_name in hashtags:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)

            post.save()
            
        
            return redirect ('feed')
    else:
        print("unseccessfull")
        form = PostForm()
    return render(request,"BlogApp/create_post.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect(reverse('login'))