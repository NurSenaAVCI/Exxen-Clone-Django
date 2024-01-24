from django.shortcuts import render, redirect
from user.models import *
from django.contrib.auth.decorators import login_required
from .models import *
from user.models import Profile
from user.forms import PasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required(login_url="/login/")
def home_page(request, profile_slug):    
    profile = Profile.objects.get(slug = profile_slug)
    profiles = Profile.objects.all()
    movies = Movies.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {
        'movies':movies,
        'profiles':profiles,
        'profile':profile,
        'categories':categories
    })

def password_change_view(request, user_username):
    
    profiles = request.user.profile_set.all()
    
    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            
            messages.info(request, 'Your Password Has Been Successfully Changed...')
            return redirect('login_page')
        else:
            messages.error(request, 'An error occurred, try again later.')
            return render(request, 'password_change.html', {
                'form': form,
                'profiles':profiles,
            })
            
    form = PasswordForm(request.user)
    return render(request, 'password_change.html', {
        'form': form,
        'profiles':profiles
    })

