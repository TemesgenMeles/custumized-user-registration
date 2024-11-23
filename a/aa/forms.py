from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from .models import CustomUser

class customusercreationform(UserCreationForm):
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False) 
    user_permissions = forms.ModelMultipleChoiceField(queryset=Permission.objects.all(), required=False) 
    class Meta: 
        model = CustomUser 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'groups', 'user_permissions')
        