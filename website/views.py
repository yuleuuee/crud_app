from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def user_login(request):
    return render(request,'login.html',{})

def user_signup(request):
    return render(request,'signup.html',{})

    
def user_profile(request):
    return render(request,'profile.html',{})

    
def user_logout(request):
    return render(request,'login.html',{})
    