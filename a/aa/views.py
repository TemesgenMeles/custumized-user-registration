from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from .forms import customusercreationform
from .models import CustomUser
# Create your views here.
class userrgistration(CreateView):
    model = CustomUser
    form_class = customusercreationform
    template_name = 'index.html'
    success_url = reverse_lazy('home')