from django import forms
from django.contrib.auth.forms import UserCreationForm
# model a la place encien model
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',   
        ]