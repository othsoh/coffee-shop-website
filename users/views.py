from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Profile,Address
from django.contrib.auth.decorators import login_required


# Create your views here.

def Login(request):

    if request.method == 'POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('password')

        my_user=authenticate(request,username=uname, password=pass1)
        if my_user is not None:
            login(request,my_user)
            
            return redirect('home')
        else:
            messages.success(request,f"Incorrect username or password ")

    return render(request, 'user/Login.html')

def Signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm_password')
        if pass1!=pass2:
            messages.warning(request, "Not matching passwords")
        else:
            new_user=User.objects.create_user(uname,email=email,password=pass1)
            new_user.save()
            messages.success(request,f'Hi {uname}, your account was created successfuly')
            return redirect('login')
        

    return render(request, 'user/Signup.html')
@login_required
def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url="/user/login/")
def account(request):
    user = request.user
    profile,_ = Profile.objects.get_or_create(user=user)
    address,_= Address.objects.get_or_create(user=user)

    if request.method == 'POST':
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        user.email = request.POST.get('email')
        profile.phone = request.POST.get('phone')
        address.city = request.POST.get('city')
        address.state = request.POST.get('state')
        address.zip = request.POST.get('zip')
        address.street = request.POST.get('street')
        picture = request.FILES.get('image')
        if picture:
            print("picture uploaded")
            profile.image = picture
            profile.save()
        

        profile.save()
        address.save()
        user.save()

        return redirect('/user/account')  

    context = {
        'profile': profile,
        'address' : address,
    }
    return render(request, 'user/account.html', context)

def delete_user(request):
    profile=Profile.objects.get(user=request.user)
    user=User.objects.get(username=request.user)

    user.delete()
    profile.delete()

    return redirect('login')