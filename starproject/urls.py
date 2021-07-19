from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url('register/',views.register, name='registration'),
    url('login/',auth_views.LoginView.as_view(), name='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    # url('logout/',auth_views.LogoutView.as_view(),name='logout'),
    url(r'^project_details/(?P<id>\d+)', views.display_project, name='prjctdtls'),
    url('profile/',views.profile, name='profile'),
    url('project/',views.awwards_project,name='newstarproject'),
    url(r'^review/(?P<project_id>\d+)', views.review_awward_project, name='review'), 
    url('search/', views.project_search,name='search'),
    url('api/profileb',views.ProfileList.as_view(),name='profileEndpoint'),
    url('api/projectsb',views.ProjectList.as_view(),name='projectsEndpoint')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)