from django.views.generic import View, UpdateView, FormView
from crud.constant import (
    LOGIN_TEMPLATE,
    REGISTRATION_TEMPLATE,
    PROFILE_UPDATE_SUCCESS_URL,
    PROFILE_TEMPLATE,
    LOGIN_ERROR,
    LOGIN_SUCCESS,
    SIGNUP_SUCCESS,
    PASSWORD_NOT_MATCH,
    LOGOUT_SUCCESS,
    USERS_URL,
    LOGIN_URL,
)
from crud.forms import (
    UserProfileUpdateForm,
    UserLoginForm,
    UserSignupForm,
)
from django.contrib.auth import login, logout, authenticate, models
from django.contrib.messages import info
from login_required import login_not_required
from django.shortcuts import redirect
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class LogoutView(View):

    def get(self, request):
        logout(request)
        info(request, LOGOUT_SUCCESS)
        return redirect(USERS_URL)


class ProfileView(UpdateView):
    form_class = UserProfileUpdateForm
    template_name = PROFILE_TEMPLATE

    def get_object(self):
        return models.User.objects.get(pk=self.request.user.pk)

    def get_success_url(self) -> str:
        return PROFILE_UPDATE_SUCCESS_URL.format(pk=self.request.user.pk)


@login_not_required
class LoginView(FormView):
    template_name = LOGIN_TEMPLATE
    form_class = UserLoginForm
    success_url = USERS_URL

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if not user:
            form.add_error(None, LOGIN_ERROR)
            return super().form_invalid(form)
        login(self.request, user)
        info(self.request, LOGIN_SUCCESS)
        return super().form_valid(form)


@login_not_required
class RegistrationView(FormView):
    template_name = REGISTRATION_TEMPLATE
    form_class = UserSignupForm
    success_url = LOGIN_URL

    def form_valid(self, form):
        try:
            password1 = self.request.POST.get("password1")
            password2 = self.request.POST.get("password2")
            validate_password(password1)
            if not password1 == password2:
                form.add_error(None, PASSWORD_NOT_MATCH)
                return super().form_invalid(form)
            user = form.save(commit=False)
            user.set_password(password1)
            user.save()
            info(self.request, SIGNUP_SUCCESS)
            return super().form_valid(form)
        except ValidationError as ve:
            form.add_error(None, ve)
            return super().form_invalid(form)
