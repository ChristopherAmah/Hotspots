from multiprocessing import context
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from hotspotapp.models import *
from dashboard.models import *
from hotspotapp.forms import SignupForm
from dashboard.forms import ProfileUpdateForm

# Create your views here.
def index(request):
    locations = Location.objects.all()
    slide1 = Showcase.objects.get(pk=1)
    slide2 = Showcase.objects.get(pk=2)
    # profile_data = Profile.objects.get(user__username = request.user.username)
    context = {
        'locations':locations,
        'slide1':slide1,
        'slide2':slide2,
        # 'profile_data':profile_data,
    }

    return render(request,'index.html',context)

def all_hotels(request):
    all_meals = Hotel.objects.all()
    locations = Location.objects.all()

    context = {
        'all_meals':all_meals,
        'locations':locations,
    }
    return render(request, 'all_hotels.html', context)

def locations(request):
    locations = Location.objects.all()
    profile_data = Profile.objects.get(user__username = request.user.username)

    context = {
        'locations':locations,
        'profile_data':profile_data,
    }
    return render(request, 'locations.html', context)

def single_location(request, id):
    locations = Location.objects.all()
    single_location = Hotel.objects.filter(location_id = id)
    loc_title = Location.objects.get(pk=id)
    profile_data = Profile.objects.get(user__username = request.user.username)

    context = {
        'locations':locations,
        'location': single_location,
        'loc_title': loc_title,
        'profile_data':profile_data,
    }
    return render(request, 'location.html', context)

def detail(request, id):
    locations = Location.objects.all()
    detail = Hotel.objects.get(pk=id)
    profile_data = Profile.objects.get(user__username = request.user.username)

    context = {
        'locations':locations,
        'detail':detail,
        'profile_data':profile_data,
    }
    return render(request, 'detail.html', context)

#authentication configuration
def signout(request):
    logout(request)
    return redirect('signin')

def signin(request):
    if request.method == "POST":
        myusername = request.POST['username']
        mypassword = request.POST['password']
        user = authenticate(request, username = myusername, password = mypassword)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'Username/Password is incorrect')
            return redirect('signin')
    return render(request, 'signin.html')

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        phone = request.POST['phone']
        image = request.POST['image']
        form = SignupForm(request.POST)
        if form.is_valid():
            userform = form.save()
            newuser = Profile(user = userform)
            newuser.first_name = userform.first_name
            newuser.last_name = userform.last_name
            newuser.email = userform.email
            newuser.phone = phone
            newuser.profile_pix = image
            newuser.save()
            messages.success(request, 'Signup successful!')
            login(request, userform)
            return redirect('index')
        else:
            messages.error(request, form.errors)
            return redirect('signup')

    return render(request, 'signup.html')
#authentication done

@login_required(login_url='signin')
# dashboard configuration
def profile(request):
    profile_data = Profile.objects.get(user__username = request.user.username)

    context = {
        'profile_data':profile_data
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='signin')
def profileupdate(request):
    profile_data = Profile.objects.get(user__username = request.user.username)
    form = ProfileUpdateForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Update successful')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('profileupdate')
    context = {
        'form':form,
        'profile_data':profile_data,
    }
    return render(request, 'profileupdate.html', context)

@login_required(login_url='signin')
def passwordupdate(request):
    profile_data = Profile.objects.get(user__username = request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password update successful')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('passwordupdate')

    context = {
        'profile_data':profile_data,
        'form':form,
    }

    return render(request, 'profilepassword.html', context)
# dashboard configuration done


