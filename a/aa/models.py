from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomUser(User): 
    # groups = models.ManyToManyField( 'auth.Group', related_name='customuser_set', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups' )
    
    # user_permissions = models.ManyToManyField( 'auth.Permission', related_name='customuser_set', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions' )
    def __str__(self): 
        return self.username