from django.urls import path
from communities.views import CreateCommunity, ListCommunity, SingleCommunity


app_name = "communities"


urlpatterns = [
    path("", ListCommunity.as_view(), name="community_list"),
    path("create/", CreateCommunity.as_view(), name="create_community"),
    path("posts/in/<slug>/", SingleCommunity.as_view(), name="community_detail")
]
