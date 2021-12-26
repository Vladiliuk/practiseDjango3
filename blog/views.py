from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Post

# Create your views here.
def main_page(request):
    if request.user.is_authenticated:
        posts = Post.objects.all().order_by('published_date')
    else: posts = ""
    context = {
        'posts': posts,
    }
    return render(request, 'main_page.html', context)

def register(request):
    form = UserCreationForm
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            pass
    context = {'form': form}
    return render(request, 'register.html', context)

def logout_reqest(reqest):
    logout(reqest)
    return redirect("/")

def login_reqest(reqest):
    if request.method =="POST":
        form = AuthenticationForm(reqest, data=reqest.POST)
        if form.is_valid():
             username= form.cleaned_data.get("username")
             password= form.cleaned_data.get("password")
             user = authenticate(reqest, username=username, password=password)
             if user is not None:
                 login(reqest, user)
                 return redirect('/')
    form = AuthenticationForm()
    contex = {'form' : form}
    return render(reqest, "login.html", context)
