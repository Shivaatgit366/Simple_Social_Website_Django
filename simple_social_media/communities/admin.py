from django.contrib import admin
from communities import models

# Register your models here.

# When we go to django admin page, sometimes we want to edit the Community members via "Community table" itself.
# When the members are visible in the "Community table", anybody can edit the members "in line" in the parent table itself.
# To edit child table "in line" from the "parent table", we should register the model/class as shown below. 
class CommunityMemberInline(admin.TabularInline):
    model = models.CommunityMember

admin.site.register(models.Community)  # normal way of registration.
