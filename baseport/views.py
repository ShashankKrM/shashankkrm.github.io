from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    posts = Post.objects.all()

    context = {'posts':posts}
    return render(request, 'index.html', context)

def posts(request):
    posts = Post.objects.filter(active = True)

    context = {'posts':posts}
    return render(request, 'posts.html', context)

def profile(request):
    return render(request, 'profile.html')

def post(request):
    return render(request, 'post.html')

# def index(request):
#     return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

#CRUD Views

@login_required(login_url="home")
def createPost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('posts')
    context = {'form':form}
    return render(request, 'post_form.html', context)

@login_required(login_url="home")
def updatePost(request):
    post = Post.objects.get()
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()

        return redirect('posts')
    context = {'form':form}
    return render(request, 'post_form.html', context)

def sendEmail(request):

    if request.method =='POST':

        template = render_to_string('email_template.html', {
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message']
        })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER, 
            ['sonumishra264@gmail.com']
        )

        email.fail_silently = False
        email.send()
    return HttpResponse('Email was sent')