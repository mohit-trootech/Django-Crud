from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from crud.views import (
    IndexView,
    LogoutView,
    LoginView,
    RegistrationView,
    InfoView,
    ProfileView,
    AddUser,
)
from debug_toolbar.toolbar import debug_toolbar_urls
from login_required import login_not_required

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/users"), name="index"),
    path("users", IndexView.as_view(), name="users"),
    path("add_user", AddUser.as_view(), name="add-user"),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("accounts/register", RegistrationView.as_view(), name="register"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
    path("info", InfoView.as_view(), name="info"),
] + debug_toolbar_urls()
