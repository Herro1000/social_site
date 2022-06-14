from django.contrib import messages
from django.shortcuts import redirect, render
#from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import Profile
# Create your views here.

def index(request):
    return render(request,"index.html")

def signup(request):
    if request.method  == 'POST' :
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"] 

        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken') 
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()

                 #create a profile object for the new user
                user_model = User.objects.get(username=username)
                user_profile = Profile.objects.create(user=user_model,user_id=user_model.id)
                user_profile.save()
                #return redirect('login')
                return redirect('signup')

        else:
            messages.info(request,'Password does not match')
            return redirect('signup')
           

            
        
    else:
        return render(request,"signup.html",{})