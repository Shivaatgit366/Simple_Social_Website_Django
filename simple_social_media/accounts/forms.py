from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.contrib.auth import get_user_model


# "UserCreationForm" is used to create new users. This model form is built in already.
class CustomerSignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()  # it helps to get the current model whoever is accessing the website. We get the in-built user model.
        fields = ["username", "email", "password1", "password2"]

    # if we want to use "custom labels" in the form, we should do the below technique.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display Name"
        self.fields["email"].label = "Email Address"
