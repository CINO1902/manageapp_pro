from django.contrib import admin
from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin


from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm
from django.forms.widgets import TextInput


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.helper.form_show_labels = False


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs["class"] = "test1111"
        self.fields["password"].widget.attrs["class"] = "test"


@admin.register(CustomUser)
class CustomUserAdmin(DefaultUserAdmin):
    model = CustomUser
    readonly_fields = ("id", "date_joined")
