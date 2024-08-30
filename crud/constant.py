# Django Crud Project Constants
from django.utils.translation import gettext_noop as _

# STATIC FILES, MEDIA FILE, TEMPLATES

STATIC = "static/"
MEDIA = "media/"
TEMPLATES = "templates/"
TZ_ASIA_KOLKATA = "Asia/Kolkata"
EN_US = "en-us"
SPANISH = "es"
FRENCH = "fr"
STATIC_DIRS = "templates/static"
# Debug Toolbar

DEBUG_TOOLBAR_IP = "127.0.0.1"

# Template Names
USER_ROW_TEMPLATE = "user_row.html"
HOME_TEMPLATE = "home.html"
LOGIN_TEMPLATE = "login.html"
REGISTRATION_TEMPLATE = "register.html"
INFO_TEMPLATE = "info.html"
PROFILE_TEMPLATE = "profile.html"

# Placeholders Form
LOGIN_FORM_USERNAME_PLACEHOLDER = _("Please Enter Login Username")
LOGIN_FORM_USERNAME_HELP_TEXT = _("Please Enter Login Username")
LOGIN_FORM_PASSWORD_PLACEHOLDER = _("Please Enter Login Password")
LOGIN_FORM_PASSWORD_HELP_TEXT = _("Password is Required")


USER_UPDATE_PLACEHOLDER = {
    "first_name": _("Please Enter First Name"),
    "last_name": _("Please Enter Last Name"),
    "email": _("Please Enter Email"),
}

USER_CREATE_PLACEHOLDER = {
    "first_name": _("Please Choose First Name"),
    "last_name": _("Please Choose Last Name"),
    "email": _("Please Choose Email"),
    "username": _("Please Choose Username"),
}

CRUD_USER_CREATE_PLACEHOLDER = {
    "title": _("Please Choose Full Name"),
    "age": _("Please Enter Age"),
}


USER_UPDATE_HELP_TEXT = {
    "first_name": _("First Name is Required Field"),
    "last_name": _("Last Name is Required Field"),
    "email": _("Email is Required Field"),
}
USER_CREATE_HELP_TEXT = {
    "email": _("Please Enter Correct Email Format"),
    "username": _("Username is Required Field"),
}

# URLS
PROFILE_UPDATE_SUCCESS_URL = "/profile/{pk}"

# Error
LOGIN_ERROR = _("Failed to Login Try Again with Correct Credentials")
PASSWORD_NOT_MATCH = _("Please Check Passwords are Not Matching")
UNIQUE_USER_ERROR = _("User with Same Username or Password Already Exists")

# Success
LOGIN_SUCCESS = _("Logged in Successfully")
SIGNUP_SUCCESS = _("User Registered Successfully")
LOGOUT_SUCCESS = _("User Logged Out Successfully")

# Cache Variables
CACHE_TABLE_NAME = "cache_table"

# Context Object Names
USERS = "users"

# URLS
USERS_URL = "/core/users"
LOGIN_URL = "/accounts/login"

# Response Status
STATUS_200 = 200
STATUS_202 = 202
STATUS_400 = 400
STATUS_404 = 404
STATUS_500 = 500

# Response Content
USER_ADDED_SUCCESS = _("User Added Successfully")
INVALID_JSON = _("Invalid JSON data")
USER_NOT_EXIST = _("User Does Not Exists")
USER_UPDATE_SUCCESS = _("User updated successfully")
