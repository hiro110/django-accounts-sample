from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'accounts'
urlpatterns = [
#    path('', views.index, name='index'),
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('login/', auth_views.login, {'template_name': 'accounts/login.html'},  name='login'),
    path('logout/', auth_views.logout, name='logout'),
]
