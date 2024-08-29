from login_required import login_not_required
from crud.constant import (
    HOME_TEMPLATE,
    USERS,
    USER_ROW_TEMPLATE,
    INFO_TEMPLATE,
    UNIQUE_USER_ERROR,
    USER_ADDED_SUCCESS,
    STATUS_200,
    STATUS_202,
    STATUS_400,
    STATUS_404,
    STATUS_500,
    INVALID_JSON,
    USER_ADDED_SUCCESS,
    USER_NOT_EXIST,
    USER_UPDATE_SUCCESS,
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
                    "status": STATUS_200,
                    "message": USER_ADDED_SUCCESS,
                    "content": response,
                }
            )
        except UniqueUserError:
            return JsonResponse(
                {"message": UNIQUE_USER_ERROR, "status": STATUS_202},
            )
        except json.JSONDecodeError:
            return JsonResponse({"message": INVALID_JSON, "status": STATUS_400})
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=500)

    def delete(self, request, *args, **kwargs):
        """
        handles delete request for user deletion
        """
        try:
            delete_crud_user_object(kwargs.get("id"))
            return JsonResponse({"status": STATUS_200})
        except User.DoesNotExist:
            return JsonResponse({"message": USER_NOT_EXIST}, status=STATUS_404)
        except json.JSONDecodeError:
            return JsonResponse({"message": INVALID_JSON}, status=STATUS_404)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=STATUS_500)

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
                    "status": STATUS_200,
                    "message": USER_UPDATE_SUCCESS,
                    "content": user_obj,
                }
            )
        except User.DoesNotExist:
            return JsonResponse({"message": USER_NOT_EXIST, "status": STATUS_404})
        except json.JSONDecodeError:
            return JsonResponse({"message": INVALID_JSON, "status": STATUS_400})
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=STATUS_500)


@login_not_required
class InfoView(TemplateView):
    """
    InfoView class to provide template for Project Information
    """

    template_name = INFO_TEMPLATE
