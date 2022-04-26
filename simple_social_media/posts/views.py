from pyexpat.errors import messages
from select import select
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from posts import models
from posts import forms
from braces.views import SelectRelatedMixin
from typing import Dict, Any

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.


class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ("user", "community")  # in the tuple, provide the foreign key columns.
    template_name = "posts/post_list.html"
    context_object_name = "list_of_post_objects"


class UserPosts(generic.ListView):
    model = models.Post
    template_name = "posts/user_post_list.html"

    # Remember "queryset" returns a "list" of objects. Queryset is inherited from its ancestor classes.
    # "get_queryset" function is present already in the table/class. If we want to change any property of the table/class, then we can use it.
    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(username__iexact=self.kwargs.get("username"))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()  # this line returns all the posts created by the user.

    # context dictionary "key" can be used in html template tags.
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context

    
class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ("user", "community")  # in the tuple, provide the foreign key columns.
    context_object_name = "post"  # this line is not required since this CBV creates the object "post" automatically.

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get("username"))


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ("message", "community")
    model = models.Post

    # below function returns HttpResponse.
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ("user", "community")
    success_url = reverse_lazy("posts:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
