from typing import Any, Dict
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import *

class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':"E-Posta"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Şifre'}))

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username','email','password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].required = False


        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control input-placeholder ' })
        self.fields['email'].widget = widgets.EmailInput(attrs={'class': 'form-control input-placeholder'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control input-placeholder', })
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control input-placeholder'})


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'name',)

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image'].widget = widgets.FileInput(attrs={'class': 'profile-img'})
        self.fields['name'].widget = widgets.TextInput(attrs={'class': 'form-control input-placeholder2'})


class PasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['old_password','new_password1','new_password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].required = False

            if fieldname == 'old_password':
                self.fields[fieldname].label = 'Güncel Şifreniz'
                
            elif fieldname == 'new_password1':
                self.fields[fieldname].label = 'Yeni Şifre'

            elif fieldname == 'new_password2':
                self.fields[fieldname].label = 'Yeni Şifreyi Tekrar Edin'
        
        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'class': 'password-input', 'placeholder': '******'})
        self.fields['new_password1'].widget = widgets.PasswordInput(attrs={'class':'password-input', 'placeholder': '******'})
        self.fields['new_password2'].widget = widgets.PasswordInput(attrs={'class':' password-input', 'placeholder': '******'})










    
    

    
    



