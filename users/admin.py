from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    """
    Extending the existing UserAdmin class to use our new CustomUser model.
    """

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "profile_picture",
        "registered_at",
        "is_staff",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
