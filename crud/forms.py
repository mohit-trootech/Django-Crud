from django.forms import (
    ModelForm,
    EmailInput,
    TextInput,
    Form,
    CharField,
    PasswordInput,
    NumberInput,
    Select,
)
from django.contrib.auth.models import User
from crud.constant import (
    USER_UPDATE_PLACEHOLDER,
    USER_UPDATE_HELP_TEXT,
    USER_CREATE_PLACEHOLDER,
    USER_CREATE_HELP_TEXT,
    CRUD_USER_CREATE_PLACEHOLDER,
)
from django.contrib.auth.forms import UserCreationForm
from core.models import CrudUser


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
                    "required": True,
                }
            )
            help_text[field] = USER_UPDATE_HELP_TEXT[field]


class UserLoginForm(Form):
    username = CharField(
        required=True,
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Please Enter Login Username",
            }
        ),
        help_text="Username is Required",
    )
    password = CharField(
        required=True,
        widget=PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Please Enter Login Password",
            }
        ),
        help_text="Password is Required",
    )


class UserSignupForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
        ]
        widgets = {}
        help_text = {}
        for field in fields:
            input_type = TextInput
            if field == "email":
                input_type = EmailInput
            widgets[field] = input_type(
                attrs={
                    "class": "form-control",
                    "placeholder": USER_CREATE_PLACEHOLDER[field],
                    "required": (False if field not in ["username"] else True),
                }
            )
            if field in ["username", "email"]:
                help_text[field] = USER_CREATE_HELP_TEXT[field]


class CrudUserForm(ModelForm):
    class Meta:
        model = CrudUser
        fields = [
            "title",
            "age",
            "status",
        ]
        widgets = {}
        for field in fields:
            input_type = TextInput
            if field == "age":
                input_type = NumberInput
            elif field == "status":
                input_type = Select
            if not field == "status":
                widgets[field] = input_type(
                    attrs={
                        "class": "form-control",
                        "placeholder": CRUD_USER_CREATE_PLACEHOLDER[field],
                        "required": True,
                    }
                )
            else:
                widgets[field] = input_type(
                    attrs={
                        "class": "form-control",
                        "required": True,
                    }
                )
