from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def user_login(request):
    # check to see if the user is logged in :
    if request.method == 'POST':
        u_name = request.POST['user_name']
        p_word = request.POST['password']

        # authenticating user
        user = authenticate(request,username =u_name, password = p_word)
        if user is not None:
            login(request,user)
            messages.success(request, "Succesfully logged in!")
            # return redirect('profile',)
            return render(request,'profile.html',{'user':user})
        else:
            messages.success(request, "Error logging in!")
            return redirect('login')
    else:
        return render(request,'login.html',{})
    


def user_signup(request):
    return render(request,'signup.html',{})

@login_required(login_url='home')    
def user_profile(request):
    return render(request,'profile.html',{})
    


@login_required(login_url='login')     
def user_logout(request):
    logout(request)
    messages.success(request,'Succesfully logged out!')
    return redirect('login')
    