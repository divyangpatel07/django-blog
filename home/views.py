from blog.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect

from .models import Contact


# Html pages
def home(request):
    return render(request, 'home/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form Correctly!")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been sent successfully")
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')


def search(request):
    query = request.GET['query']
    allPosts = Post.objects.filter(title__icontains=query)
    return render(request, 'home/search.html', {'allPosts': allPosts, 'query': query})


# Authntication APIs
def handleSignup(request):
    if request.method == 'POST':
        # Get post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if len(username) > 10:
            messages.error(request, "Username must be under 10 Character")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username should only contains letters and numbers")
            return redirect('home')
        if pass1 != pass2:
            messages.success(request, "Password do not match")
            return redirect('home')

        # check for errorneous inputs
        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse('404-Not Found')


def handleLogin(request):
    if request.method == 'POST':
        # Get post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect(home)
        else:
            messages.error(request, 'Invalid credentials,Please try again')
            return redirect(home)
    return HttpResponse('404-Not Found')


def handleLogout(request):
    logout(request)
    messages.success(request, 'Succesfully logged out')
    return redirect(home)
    return HttpResponse("handle logout")
