from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from newapp.models import *

# Create your views here.

def index(request):
    args = {
        'user': request.user.username,
        "posts": Post.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request,"base_dir.html",args)
def all_comments(request):
    context ={
        "comments": Comment.objects.all()
    }
    return render(request,"comments.html",context)


def article(request,article_id):
    new_article = Post.objects.get(id = article_id)
    print new_article.title
    args = {
      
        'article' : new_article,
        "comments": Comment.objects.filter(post_comment_id=article_id),
        'categories': Category.objects.all(),

    }
    return render(request,'post_dir.html',args)

def category(request,category_id):
    context ={
        'category': Category.objects.get(id=category_id),
        'categories' : Category.objects.all(),
        'posts':  Post.objects.filter(category_id=category_id)
    }
    return render(request,'category.html',context)
def add_comment(request, id):
    author = request.POST.get('author')
    text = request.POST.get('comment')
    comment = Comment.objects.create(autor = author, text = text, post_comment_id = id)
    comment.save()
    return redirect('/article/%s/'% id)


def reg(request):

    return render(request,'registra'
                          'tion.html')


def add_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User.objects.create_superuser(username = username,email="k@m.ru", password = password)
    user.save()
    return redirect('/auth/')


def auth(request):
    return render(request, 'auth.html')


def log_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username = username, password = password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('/auth/')


def log_out(request):
    logout(request)
    return redirect('/')
