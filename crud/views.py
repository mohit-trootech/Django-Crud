from django.db.models.query import QuerySet
from django.views.generic import ListView, View, TemplateView, UpdateView
from crud.constant import (
    HOME_TEMPLATE,
    LOGIN_TEMPLATE,
    REGISTRATION_TEMPLATE,
    USER_ROW_TEMPLATE,
    INFO_TEMPLATE,
    PROFILE_UPDATE_SUCCESS_URL,
    PROFILE_TEMPLATE,
)
from crud.forms import UserProfileUpdateForm
from django.contrib.auth import login, logout, authenticate, models


class IndexView(ListView):
    model = models.User
    template_name = HOME_TEMPLATE
    context_object_name = "users"
    paginate_by = 20
    ordering = ["id"]

    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            return USER_ROW_TEMPLATE
        else:
            return self.template_name


class LogoutView(View):

    def get(self):
        logout(self.request)
        return "/login"


class ProfileView(UpdateView):
    form_class = UserProfileUpdateForm
    template_name = PROFILE_TEMPLATE

    def get_object(self):
        return models.User.objects.get(pk=self.request.user.pk)

    def get_success_url(self) -> str:
        return PROFILE_UPDATE_SUCCESS_URL.format(pk=self.request.user.pk)


class LoginView(TemplateView):
    template_name = LOGIN_TEMPLATE


class RegistrationView(TemplateView):
    template_name = REGISTRATION_TEMPLATE


class InfoView(TemplateView):
    template_name = INFO_TEMPLATE
