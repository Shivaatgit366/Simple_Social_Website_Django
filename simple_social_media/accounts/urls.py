from accounts import views
from django.urls import path
import accounts
from accounts.views import SignUp
from django.contrib.auth import views as auth_views


app_name = "accounts"


urlpatterns = [
    path("signup/", SignUp.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="user_login"),
    path("logout/", auth_views.LogoutView.as_view(), name="user_logout")
]
