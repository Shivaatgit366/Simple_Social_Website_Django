from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from accounts.models import User
from django.urls import reverse_lazy, reverse
from accounts.forms import CustomerSignUpForm


# Create your views here.

class HomePage(TemplateView):
    template_name = "index.html"


class TestPage(TemplateView):
    template_name = "test.html"


class ThanksPage(TemplateView):
    template_name = "thanks.html"


class SignUp(CreateView):
    # this "CreateView" cbv creates a model-form. We should specify the model name and fields to be displayed.
    # if we have already created a form/model-form, then we should just mention it as "form_class".

    # after the sign-up, page should be redirected to "login" page.
    model = User
    form_class = CustomerSignUpForm
    success_url = reverse_lazy('accounts:user_login')

    # even though "templates directory" is different, django automatically finds the template file in the below directory.
    template_name = "accounts/signup.html"
