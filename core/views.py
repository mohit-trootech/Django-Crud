from login_required import login_not_required
from core.models import CrudUser
from crud.constant import (
    HOME_TEMPLATE,
    USERS,
    USER_ROW_TEMPLATE,
    INFO_TEMPLATE,
    USER_ADDED_SUCCESS,
)
from django.views.generic import ListView, View, TemplateView
import json
from core.utils import create_crud_user_object, delete_crud_user_object
from django.http import JsonResponse


class IndexView(ListView):
    model = CrudUser
    template_name = HOME_TEMPLATE
    context_object_name = USERS
    paginate_by = 10

    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            return USER_ROW_TEMPLATE
        else:
            return self.template_name


class AddUser(View):

    def post(self, request):
        data = json.loads(request.POST.get("data"))
        obj = create_crud_user_object(data)
        response = {
            "id": obj.get("id"),
            "title": obj.get("title"),
            "age": obj.get("age"),
            "status": "Active" if obj.get("status") else "Unactive",
            "content": USER_ADDED_SUCCESS,
        }
        return JsonResponse(response)


class DeleteUser(View):

    def post(self, request):
        data = json.loads(request.POST.get("data"))
        response = delete_crud_user_object(data.get("id"))
        return JsonResponse(response)


@login_not_required
class InfoView(TemplateView):
    template_name = INFO_TEMPLATE
