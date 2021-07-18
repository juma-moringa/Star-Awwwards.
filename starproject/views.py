from django.http.response import HttpResponseRedirect
from starproject.models import Profile, Project, Review
from django.contrib.auth.models import User
from starproject.forms import ProfileForm, ProjectsForm, ReviewsForm, SignUpForm
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

def rate_selected_project(request,project_id):
    select_projct = Project.review_project_by_id(id=project_id)
    project = get_object_or_404(Project, pk=project_id)
    current_user = request.user
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            usability = form.cleaned_data['usability']
            design = form.cleaned_data['design']
            content = form.cleaned_data['content']
            rate_selected = Review()
            rate_selected.project = project
            rate_selected.user = current_user
            rate_selected.design = design
            rate_selected.usability = usability
            rate_selected.content = content
            rate_selected.average = (rate_selected.design + rate_selected.usability + rate_selected.content)/3
            rate_selected.save()
            # return HttpResponseRedirect(reverse('projectdetails', args=(project.id,)))
            return redirect('index')
    else:
        form = ReviewsForm()
    return render(request, 'reviews.html', {"project":select_projct,"user":current_user,"form":form})