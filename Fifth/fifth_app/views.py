from django.shortcuts import render
from fifth_app.forms import UserFrom,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    return render(request,'fifth_app/index.html')

@login_required
def special(request):
    return HttpResponse("You'r logging In ")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserFrom(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user =user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user= user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form =UserFrom()
        profile_form = UserProfileInfoForm()

    return render(request,'fifth_app/register.html',{'user_form': user_form,'profile_form':profile_form,'registered':registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                HttpResponse("Account NOt ACtive")

        else:
            print('Someone try to login and failed')
            print('username: {} and password: {}'.format(username,password))
            return HttpResponse("Invalid Login details")

    else:
        return render(request,'fifth_app/login.html',{})
