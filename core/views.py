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
    update_user_data,
)
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class IndexView(ListView):
    """
    IndexView class to show the users data with the custom specification as class attributes
    """

    model = User
    template_name = HOME_TEMPLATE
    context_object_name = USERS
    paginate_by = 10
    ordering = ["-date_joined"]

    def get_template_names(self) -> list[str]:
        """
        infinite scrolling with django htmx, request for template with row when last object trigger in html
        """
        if self.request.htmx:
            return USER_ROW_TEMPLATE
        else:
            return self.template_name


@method_decorator(csrf_exempt, name="dispatch")
class HandleUser(View):

    def post(self, request, *args, **kwargs):
        """
        handles post request for user creation
        """
        try:
            data = json.loads(request.POST.get("data"))
            user_obj = create_crud_user_object(data)
            response = serialize_response_data(user_obj)
            return JsonResponse(
                {
                    "status": 200,
                    "message": "user Created Successfully",
                    "content": response,
                }
            )
        except UniqueUserError:
            return JsonResponse(
                {"content": UNIQUE_USER_ERROR},
                status=202,
            )
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=500)

    def delete(self, request, *args, **kwargs):
        """
        handles delete request for user deletion
        """
        try:
            delete_crud_user_object(kwargs.get("id"))
            return HttpResponse(status=200)
        except User.DoesNotExist:
            return JsonResponse({"message": "User Does Not Exists"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=500)

    def put(self, request, *args, **kwargs):
        """
        handles update request for user updation
        """
        try:
            data = json.loads(request.body)
            id = kwargs.get("id")
            user = User.objects.get(id=id)
            user_obj = update_user_data(user=user, data=data)
            return JsonResponse(
                {
                    "status": 200,
                    "message": "User updated successfully",
                    "content": user_obj,
                }
            )
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=500)


@login_not_required
class InfoView(TemplateView):
    """
    InfoView class to provide template for Project Information
    """

    template_name = INFO_TEMPLATE
