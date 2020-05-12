from django.shortcuts import render, redirect, HttpResponse
from .models import *
# from django.contrib import messages

def index(request):
    if request.method == "GET":
        return render(request, 'index.html')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    if request.method == "POST":
        new_user = User.objects.create(
            first_name=request.POST['FirstName'],
            last_name=request.POST['LastName'],
            email=request.POST['Email'],
            image = request.POST['Profile_Picture'],
            password=request.POST['Password']
        )
        print("image url", new_user.image.url)
        request.session['id'] = new_user.id
        print("session id", request.session['id'])
        return redirect('/dashboard')


def dashboard(request):
    if 'id' not in request.session:
        return redirect("/")
    if request.method == "GET":
        user = User.objects.get(id=request.session['id'])
        all_users = User.objects.all()
        all_posts = Status.objects.all().order_by('-created_at')
        all_comments = Comment.objects.all()
        context ={
            "user": user,
            "all_users" : all_users,
            "all_posts" : all_posts,
            "all_comments": all_comments,
        }
        return render(request, 'dashboard.html', context)

def post_status(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id = request.session['id'])
        new_post = Status.objects.create(
            status=request.POST['status_update'],
            user_post= user,
             likes = 0)
        return redirect("/dashboard")

# Needs to implement feature that associates like with user.
def like_status(request, post_id):
    if 'id' not in request.session:
        return redirect("/")
    if request.method == 'GET':
       post = Status.objects.get(id = post_id)
       user = User.objects.get(id = request.session['id'])
       post.likes += 1
       post.save() 
       print(post.likes)
       return redirect("/dashboard")

def post_comment(request, post_id):
    if 'id' not in request.session:
        return redirect("/")
    if request.method == "POST":
        post = Status.objects.get(id = post_id) 
        user = User.objects.get(id = request.session['id'])
        new_comment = Comment.objects.create(
            comment = request.POST['comment'],
            status = post,
            user_comment = user)
        return redirect("/dashboard")
    
def delete_comment(request, post_id):
    if 'id' not in request.session:
        return redirect("/")
    if request.method == 'GET':
        comment = Comment.objects.get(id = post_id)
        comment.delete()
        return redirect("/dashboard")

#BUG when profile is updated, jinja displays ('username') adding parenthesis and quotes
def edit_profile(request, user_id):
    if 'id' not in request.session:
        return redirect("/")
    if request.method == 'GET':
        user = User.objects.get(id=request.session['id'])
        context ={
            "user": user,
        }
        return render(request, 'edit_profile.html', context)
    if request.method == 'POST':
        user = User.objects.get(id = user_id)
        user.first_name=request.POST['FirstName'],
        user.last_name=request.POST['LastName'],
        user.email=request.POST['Email'],
        user.save()
        return redirect ("/dashboard")
        

# def change_password(request, user_id):
#     return redirect('/dashboard')    

