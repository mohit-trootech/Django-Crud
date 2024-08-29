from login_required import login_not_required
from crud.constant import (
    HOME_TEMPLATE,
    USERS,
    USER_ROW_TEMPLATE,
    INFO_TEMPLATE,
    UNIQUE_USER_ERROR,
)
from core.exceptions import UniqueUserError
from django.views.generic import ListView, View, TemplateView
import json
from core.utils import (
    create_crud_user_object,
    delete_crud_user_object,
    serialize_response_data,
)
from django.http import JsonResponse
from django.contrib.auth.models import User


class IndexView(ListView):
    model = User
    template_name = HOME_TEMPLATE
    context_object_name = USERS
    paginate_by = 10
    ordering = ["-date_joined"]

    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            return USER_ROW_TEMPLATE
        else:
            return self.template_name


class HandleUser(View):

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.POST.get("data"))
            user_obj = create_crud_user_object(data)
            print(user_obj)
            response = serialize_response_data(user_obj)
            response["csrftoken"] = request.COOKIES.get("csrftoken")
            return JsonResponse({"status": 200, "content": response})
        except UniqueUserError:
            return JsonResponse({"status": 202, "content": UNIQUE_USER_ERROR})

    def delete(self, request, *args, **kwargs):
        response = delete_crud_user_object(kwargs.get("id"))
        return JsonResponse(response)


@login_not_required
class InfoView(TemplateView):
    template_name = INFO_TEMPLATE
