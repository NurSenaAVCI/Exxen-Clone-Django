from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_page'),
    path('login/', login_view, name='login_page'),
    path('register1/', register_view, name='register1_page'),
    path('logout/', logout_view, name='logout_page'),
    path('profile/', profile_view, name='profile_page'),
    path('profile_add/', profile_add_view, name='profile_add_page'),
    path('profile-edit/<slug:profile_slug>/', profile_edit_view, name="profile_edit_page"),
    path('profile_delete/<slug:profile_slug>/', profile_delete_view, name="profile_delete_page"),
    
    ]