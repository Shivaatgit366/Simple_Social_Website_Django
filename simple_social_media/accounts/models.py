from django.db import models
from django.contrib import auth

# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):
    
    # string representation of the object. To get the feel like Twitter, we are using "@username".
    # This model is same as in-built model "auth.models.User", only thing we want to change the appearance of the username to "twitter like username".
    def __str__(self):
        return "@{}".format(self.username)
