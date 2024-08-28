from django.forms import ModelForm, EmailInput, TextInput
from django.contrib.auth.models import User
from crud.constant import USER_UPDATE_PLACEHOLDER, USER_UPDATE_HELP_TEXT


class UserProfileUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {}
        help_text = {}

        for field in fields:
            input_type = TextInput
            if field == "email":
                input_type = EmailInput
            widgets[field] = input_type(
                attrs={
                    "class": "form-control",
                    "placeholder": USER_UPDATE_PLACEHOLDER[field],
                }
            )
            help_text[field] = USER_UPDATE_HELP_TEXT[field]
