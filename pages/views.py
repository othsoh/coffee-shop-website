from django.shortcuts import redirect, render
from django.contrib import messages
from users.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/user/login/")
def home(request):
   
    return render(request, 'home/index.html')

@login_required(login_url="/user/login/")
def about(request):
    
    return render(request, 'home/about.html')




