from django import forms, views
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from posts import models
from posts import forms
from braces.views import SelectRelatedMixin

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.


class PostList(SelectRelatedMixin, generic.ListView):
    pass