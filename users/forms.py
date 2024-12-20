from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    The UserCreationForm is linked with the User class. Used to create new users  # noqa: E501
    """

    email = forms.EmailField(required=True, max_length=300)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    """
    The UserchangeForm is related to changing users rights at the admin page.  # noqa: E501
    """

    email = forms.EmailField(required=True, max_length=300)

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ("email",)
