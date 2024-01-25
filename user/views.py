from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from movie.models import Movies
from django.contrib.auth.models import User

def index_view (request):
    movies = Movies.objects.all()
    forms = UserLoginForm()

    if request.method == 'POST':
        return redirect('register1_page')
    
    return render(request, 'index.html', {
        'forms': forms,
        'movies':movies
    })

    
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = User.objects.get(email = email).username
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                messages.success(request, 'Login Succesfully!')
                return redirect('profile_page')
            
            else:
                messages.warning(request, 'User not found')
                return render (request, 'login.html', {
                    'form' : form})
            
        else:
            return render (request, 'login.html', {
                'form' : form})

    else:
        form = UserLoginForm()
        return render (request, 'login.html', {
            'form' : form
        })


def register_view(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST or None)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('profile_page')
        
            else:
                return render(request, 'register.html', {
                    'form': form,
                })
            
        else:
            return render(request, 'register.html', {
                'form': form, 'error': 'User creation failed'
            })
        
    form = SignUpForm()
    return render(request, 'register.html', {
        'form': form
    })


def logout_view(request):
    logout(request)
    return redirect('index_page')


def profile_view(request):

    profiles = Profile.objects.filter(owner = request.user)

    return render(request, 'profile.html', {
        'profiles': profiles
    })


def profile_add_view(request):

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.owner = request.user
            profile.save()
            messages.success(request, 'Profile created.')
            return redirect('profile_page')
        else:
            messages.error(request, 'Profile not created.')
            return render(request, 'profile_add.html', {
                'form': form
            })

    form = UserProfileForm()
    return render(request, 'profile_add.html', {
        'form': form
    })


def profile_edit_view(request, profile_slug):

    profile = Profile.objects.get(slug = profile_slug)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.owner = request.user
            profile.save()
            messages.success(request, 'Replacement Successful')
            return redirect('profile_page')
        else:
            return render(request, 'profile_edit.html', {
                'form': form,
                'profile': profile
            })

    form = UserProfileForm(instance=profile)
    return render(request, 'profile_edit.html', {
        'form': form,
        'profile': profile
    })


def profile_delete_view(request, profile_slug):

    profile = Profile.objects.get(slug = profile_slug)

    if request.method == 'POST':
        profile.delete()
        return redirect('profile_page')
    
    return render(request, 'profile_delete.html', {'profile': profile})





