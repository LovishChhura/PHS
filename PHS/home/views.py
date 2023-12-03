from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url="/login/")
def index(request):
    return render(request,'user_index.html')

@login_required(login_url="/login/")
def reduce_stress(request):
    return render(request,'reduce_stress.html')

@login_required(login_url="/login/")
def diet_plan(request):
    return render(request,'diet_plan.html')

# def home(request):
#     return render(request,'home.html')

def login_page(request):
    if request.method=="POST":
        username=request.POST.get('usernameL')
        password=request.POST.get('passwordL')
        
        if not User.objects.filter(username=username).exists():
            # messages.error(request,'Invalid email-id')
            return render(request,'login.html', {'from': 'login','message':'Invalid username'})
        user=authenticate(username=username,password=password)
        if user is None:
            # messages.error(request,'Invalid credentials')
            return render(request,'login.html', {'from': 'login', 'message':'Invalid credentials'})
        else:
            login(request,user)
            return redirect('/')
            
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method=="POST":
        full_name=request.POST.get('full_name')
        full_name=full_name.split()
        if len(full_name)==2:
            first_name=full_name[0]
            last_name=full_name[1]
        else:
            first_name=full_name[0]
            last_name=""
        username=request.POST.get('usernameS')
        password=request.POST.get('passwordS')
        
        user=User.objects.filter(username=username)
        if user.exists():
            # messages.info(request,'User already exist')
            return render(request,'login.html', {'from': 'signup','message':'User already exist'})
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        # messages.info(request,'Registered Successfully')
        return render(request,'login.html', {'from': 'signup','message':'Registered Successfully', 'info':'success'})
    return render(request,'login.html')