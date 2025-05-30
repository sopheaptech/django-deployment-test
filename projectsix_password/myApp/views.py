from django.shortcuts import render
from myApp.forms import UserInfoForm, UserProfileInfoForm



# Import some importan functionality of login and Log out
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse 
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
  return render(request,'myApp/index.html')


def register(request):
  registered=False # the user dons't register yet

  if request.method == "POST":
    user_form= UserInfoForm(data=request.POST)
    profile_form=UserProfileInfoForm(data=request.POST)

    if user_form.is_valid() and profile_form.is_valid():
      user=user_form.save()
      user.set_password(user.password)
      user.save()

      profile=profile_form.save(commit=False)
      profile.user=user # this line of code make profile one to one relationship to user from the models
      
      if 'profile_pic' in request.FILES:
        profile.profile_pic=request.FILES['profile_pic']
      profile.save()

      registered=True # the user has been registered
    else:
      print(user_form.errors,profile_form.errors)
  else:
    user_form=UserInfoForm()
    profile_form=UserProfileInfoForm()
  return render(request,'myApp/registration.html',{
    'user_form':user_form,'profile_form':profile_form,'registered':registered
  })


# User Login Request 

def user_login(request):
  if request.method=='POST':
    username=request.POST.get('username') # username from HTML file login
    password=request.POST.get('password') # password from HTML file login

    # User Authetication
    user=authenticate(username=username,password=password)
    if user: # if user pass the authentication log user in
      if user.is_active:
        login(request,user)
        return HttpResponseRedirect(reverse('index')) # After Login redirect user to home page
      else:
        return HttpResponse('ACOUNT NOT ACTIVE!')
    else:
      print("Someone tried to login but fail!")
      print(f"Username: {username} and Password: {password}")
      return HttpResponse("Invalid login details supplied!")
  else:
    return render(request,'myApp/login.html',{})

@login_required
def user_logout(request):
  logout(request)
  return HttpResponseRedirect(reverse('index'))


