from django.http.response import HttpResponseRedirect
from starproject.models import Profile, Project, Review
from django.contrib.auth.models import User
from starproject.forms import ProfileForm, ProjectsForm, SignUpForm
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    profiles = Profile.objects.all()
    projects = Project.objects.all()
    return render( request,'index.html',{"profiles":profiles,"projects":projects})

@login_required(login_url='/accounts/login/')
def awwwards_profile(request):
    return render( request,'index.html')

def register(request):
    if request.method=="POST":
        form=SignUpForm(request.POST) 
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           user_password = form.cleaned_data.get('password1')
           user = authenticate(username=username, password=user_password)
           login(request, user)
        return redirect('login')
    else:
        form= SignUpForm()
    return render(request, 'registration/registration_form.html', {"form":form})  

@login_required(login_url='/accounts/login/')    
def profile(request):
    if request.method == 'POST':
        user_profile_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if  user_profile_form.is_valid():
            user_profile_form.save()
            return redirect('home')
    else:
        user_profile_form = ProfileForm(instance=request.user)
        # user_form = UserProfileUpdateForm(instance=request.user)
    return render(request, 'profile.html',{"user_profile_form": user_profile_form})

@login_required(login_url='/accounts/login')
def awwards_project(request):
	current_user = request.user
	if request.method == 'POST':
		form = ProjectsForm(request.POST,request.FILES)
		if form.is_valid():
			awwards_project = form.save(commit=False)
			awwards_project.user = current_user
			awwards_project.save()
			return redirect('index')
	else:
			form = ProjectsForm()
	return render(request, 'starprojects.html',{"form":form})

@login_required(login_url='/accounts/login')
def display_project(request,id):
    project = Project.objects.get(id = id)
    reviews = Review.objects.all()
    return render(request, 'displayproject.html',{"reviews":reviews,"project":project})




