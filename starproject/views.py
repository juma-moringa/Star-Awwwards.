from starproject.serializer import ProfileSerializer
from django.http.response import HttpResponseRedirect
from starproject.models import Profile, Project, Review
from django.contrib.auth.models import User
from starproject.forms import ProfileForm, ProjectsForm, ReviewsForm, SignUpForm
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework import serializers
from .models import Profile,Project
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

def index(request):
    profiles = Profile.objects.all()
    projects = Project.objects.all()
    reviews = Review.objects.all()
    return render( request,'index.html',{"profiles":profiles,"projects":projects ,'reviews':reviews})

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

@login_required(login_url='/accounts/login/')
def review_project(request,project_id):
    rvw_proj = Project.project_by_id(id=project_id)
    project = get_object_or_404(Project, pk=project_id)
    current_user = request.user
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            review = Review()
            review.project = project
            review.user = current_user
            review.design = design
            review.usability = usability
            review.content = content
            review.average = (review.design + review.usability + review.content)/3
            review.save()
            return HttpResponseRedirect(reverse('prjctdtls', args=(project.id,)))
    else:
        form = ReviewsForm()
    return render(request, 'reviews.html', {"user":current_user,"project":rvw_proj,"form":form})

@login_required(login_url='/accounts/login/')
def project_search(request): 
    if 'search_title' in request.GET and request.GET['search_title']:
        p_title = request.GET.get("search_title")
        searchResults = Project.search_projects(p_title)
        message = f'P_title'
        results=searchResults
        message = message
        return render(request,'projectsearch.html', {'results':results,'message':message})
    else:
        message = "Your search did not match any project titles onboard."
    return render(request, 'projectsearch.html', {'message': message})

# class MerchList(APIView):
#     def get(self, request, format=None):
#         all_merch = MoringaMerch.objects.all()
#         serializers = MerchSerializer(all_merch, many=True)
#         return Response(serializers.data) 



class ProfileList(APIView):
   
    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

