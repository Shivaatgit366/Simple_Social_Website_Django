from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from communities.models import Community, CommunityMember
from django.contrib import messages


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

    # "context_object_name" is the "key" in the context dictionary. This key will be used in template tag.
    # "context_object_name" gives list of objects in this case.
    # "ListView" provides us a list of objects.
    context_object_name = "list_of_community_objects"


class JoinCommunity(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("communities:community_detail", kwargs={"slug":self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        community = get_object_or_404(Community, slug=self.kwargs.get("slug"))

        try:
            CommunityMember.objects.create(user=self.request.user, community=community)
        except IntegrityError:
            messages.warning(self.request, "Warning already a member!!")
        else:
            messages.success(self.request, "You are now a member!!")
        return super().get(request, *args, **kwargs)


class LeaveCommunity(LoginRequiredMixin, generic.RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse("communities:community_detail", kwargs={"slug":self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:
            membership = CommunityMember.objects.filter(
                user = self.request.user,
                community__slug = self.kwargs.get("slug")
            ).get()
        except CommunityMember.DoesNotExist:
            messages.warning(self.request, "Sorry, you are not in this community!!")
        else:
            membership.delete()
            messages.success(self.request, "You have left the community!!")
        
        return super().get(request, *args, **kwargs)
