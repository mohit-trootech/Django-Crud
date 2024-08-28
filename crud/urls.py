from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from crud.views import IndexView, LogoutView, LoginView, RegistrationView, InfoView
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/users"), name="index"),
    path("users", IndexView.as_view(), name="users"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("register", RegistrationView.as_view(), name="register"),
    path("info", InfoView.as_view(), name="info"),
] + debug_toolbar_urls()
