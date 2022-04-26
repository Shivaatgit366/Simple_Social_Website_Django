from django.urls import path
from communities.views import CreateCommunity, ListCommunity, SingleCommunity, JoinCommunity, LeaveCommunity


app_name = "communities"


urlpatterns = [
    path("", ListCommunity.as_view(), name="community_list"),
    path("create/", CreateCommunity.as_view(), name="create_community"),
    path("members_and_posts/in/<slug>/", SingleCommunity.as_view(), name="community_detail"),
    path("join/<slug>/", JoinCommunity.as_view(), name="join_community"),
    path("leave/<slug>/", LeaveCommunity.as_view(), name="leave_community")
]
