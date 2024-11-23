from django.urls import path
from .views import userrgistration

urlpatterns = [
    path('', userrgistration.as_view(), name='home'),
]