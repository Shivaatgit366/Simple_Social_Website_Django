from django.db import models
from django.utils.text import slugify
from django import misaka
from django.urls import reverse

# this function helps us to get the current user model active in the project.
from django.contrib.auth import get_user_model
User = get_user_model()

# template module helps us to get various django template tags and other libraries.
from django import template
register = template.Library()


# Create your models here.

# create a table called "community" with various attributes.
class Community(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)  # slug creates a url based on the "given title"(in this case "community name"), so this column should also be unique.
    description = models.TextField(blank=True, default="")
    description_html = models.TextField(editable=False, blank=True, default="")  # for content in html format.
    members = models.ManyToManyField(User, through="CommunityMember")

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("communities:community_detail", kwargs={"slug":self.slug})

    class Meta:
        ordering = ["name"]


# create a table called "community member" with various attributes.
class CommunityMember(models.Model):
    community = models.ForeignKey(Community, related_name="memberships", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_communities", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        unique_together = ("community", "user")  # this is many to many relationship; both the "community" and "user" columns are taken together to form a primary key.

