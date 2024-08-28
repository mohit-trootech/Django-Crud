# Django Crud Project Constants

# STATIC FILES, MEDIA FILE, TEMPLATES

STATIC = "static/"
MEDIA = "media/"
TEMPLATES = "templates/"

# Debug Toolbar

DEBUG_TOOLBAR_IP = "127.0.0.1"

# Template Names
USER_ROW_TEMPLATE = "user_row.html"
HOME_TEMPLATE = "home.html"
LOGIN_TEMPLATE = "login.html"
REGISTRATION_TEMPLATE = "register.html"
INFO_TEMPLATE = "info.html"
PROFILE_TEMPLATE = "profile.html"

# Placeholders Update Form
USER_UPDATE_PLACEHOLDER = {
    "first_name": "Please Enter First Name",
    "last_name": "Please Enter Last Name",
    "email": "Please Enter Email",
}

USER_CREATE_PLACEHOLDER = {
    "first_name": "Please Choose First Name",
    "last_name": "Please Choose Last Name",
    "email": "Please Choose Email",
    "username": "Please Choose Username",
}

USER_UPDATE_HELP_TEXT = {
    "first_name": "First Name is Required Field",
    "last_name": "Last Name is Required Field",
    "email": "Email is Required Field",
}
USER_CREATE_HELP_TEXT = {
    "email": "Please Enter Correct Email Format",
    "username": "Username is Required Field",
}
# URLS
PROFILE_UPDATE_SUCCESS_URL = "/profile/{pk}"

# Error
LOGIN_ERROR = "Failed to Login Try Again with Correct Credentials"
PASSWORD_NOT_MATCH = "Please Check Passwords are Not Matching"

# Success
LOGIN_SUCCESS = "Logged in Successfully"
SIGNUP_SUCCESS = "User Registered Successfully"
