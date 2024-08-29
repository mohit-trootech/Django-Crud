# Django Crud Project Constants

# STATIC FILES, MEDIA FILE, TEMPLATES

STATIC = "static/"
MEDIA = "media/"
TEMPLATES = "templates/"
TZ_ASIA_KOLKATA = "Asia/Kolkata"
EN_US = "en-us"
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
LOGIN_FORM_USERNAME_PLACEHOLDER = "Please Enter Login Username"
LOGIN_FORM_USERNAME_HELP_TEXT = "Please Enter Login Username"
LOGIN_FORM_PASSWORD_PLACEHOLDER = "Please Enter Login Password"
LOGIN_FORM_PASSWORD_HELP_TEXT = "Password is Required"


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

CRUD_USER_CREATE_PLACEHOLDER = {
    "title": "Please Choose Full Name",
    "age": "Please Enter Age",
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
UNIQUE_USER_ERROR = "User with Same Username or Password Already Exists"
# Success
LOGIN_SUCCESS = "Logged in Successfully"
SIGNUP_SUCCESS = "User Registered Successfully"
LOGOUT_SUCCESS = "User Logged Out Successfully"

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
USER_ADDED_SUCCESS = "User Added Successfully"
INVALID_JSON = "Invalid JSON data"
USER_NOT_EXIST = "User Does Not Exists"
USER_UPDATE_SUCCESS = "User updated successfully"
