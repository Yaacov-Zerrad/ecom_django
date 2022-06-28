from django.forms import ModelForm
from .models import Profile
from django import forms



class ProfileForm(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    
    name = forms.CharField(  widget=forms.TextInput(
        attrs={
            'placeholder': 'Your name',
            "class": "form-control",
        }
    ))        
    email = forms.EmailField(  widget=forms.TextInput(
        attrs={
            'placeholder': 'Your email',
            "class": "form-control",
        }
    ))        
    phone = forms.CharField(  widget=forms.TextInput(
        attrs={
            'placeholder': 'Your phone',
            "class": "form-control",
        }
    ))        
    address = forms.CharField(  widget=forms.TextInput(
        attrs={
            'placeholder': 'Your address',
            "class": "form-control",
        }
    ))        
    skill = forms.CharField(  widget=forms.TextInput(
        attrs={
            'placeholder': 'Your skill',
            "class": "form-control",
        }
    ))        
    langue = forms.CharField(  widget=forms.TextInput(
        attrs={
            'placeholder': 'Your langue',
            "class": "form-control",
        }
    ))        
    interest = forms.CharField(  widget=forms.TextInput(
        attrs={
            'placeholder': 'Your interest',
            "class": "form-control",
        }
    ))        
    experience = forms.CharField(  widget=forms.TextInput(
        attrs={
            'placeholder': 'Your experience',
            "class": "form-control",
        }
    ))        
    education = forms.CharField(  widget=forms.Textarea(
        attrs={
            'placeholder': 'Your education',
            "class": "form-control",
        }
    ))        
    project = forms.CharField(  widget=forms.Textarea(
        attrs={
            'placeholder': 'Your projects',
            "class": "form-control",
        }
    ))        

        
        
        
        
    class Meta:
        model = Profile
        fields = '__all__'
    