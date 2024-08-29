from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from crud.views import (
    LogoutView,
    LoginView,
    RegistrationView,
    ProfileView,
)
from debug_toolbar.toolbar import debug_toolbar_urls
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("core/", include("core.urls")),
    path("", RedirectView.as_view(url="/core/users"), name="index"),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/register", RegistrationView.as_view(), name="register"),
    path("profile/<int:pk>", cache_page(0)(ProfileView.as_view()), name="profile"),
] + debug_toolbar_urls()
