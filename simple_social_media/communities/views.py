from dataclasses import fields
from pyexpat import model
from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from communities.models import Community, CommunityMember

# Create your views here.


class CreateCommunity(LoginRequiredMixin, generic.CreateView):
    model = Community
    fields = ["name", "description"]


class SingleCommunity(generic.DetailView):
    model = Community
    template_name = "communities/community_detail.html"

    # "context_object_name" is the "key" in the context dictionary. This key will be used in template tag.
    # "context_object_name" gives only one row object.
    # "DetailView" provides us a dictionary/object.
    context_object_name = "community_object"


class ListCommunity(generic.ListView):
    model = Community
    template_name = "communities/community_list.html"
    context_object_name = "list_of_community_objects"