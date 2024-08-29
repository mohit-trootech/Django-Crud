from django.contrib.auth.models import User
from crud.constant import UNIQUE_USER_ERROR
from django.db.models import Q
from core.exceptions import UniqueUserError


def password_check_counter_loop(password: str) -> bool:
    """
    return Assertion Error if password is True for any user objects

    :param password: str
    :return: bool
    """
    check = False
    try:
        for user in User.objects.all():
            assert check == user.check_password(password)
        return True
    except AssertionError:
        return False


def create_crud_user_object(data: dict):
    """
    create user object based on unique username & password check else UniqueUserError

    :param data: dict
    :raises UniqueUserError: BaseException
    """
    if not User.objects.filter(
        Q(username=data["username"])
    ) and password_check_counter_loop(data.get("password")):
        user_obj = User(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            username=data.get("username"),
        )
        user_obj.set_password(data.get("password"))
        user_obj.save()
        return user_obj.__dict__
    raise UniqueUserError(UNIQUE_USER_ERROR)


def serialize_response_data(user_obj: dict) -> dict:
    """
    serialize user object data for custom requirements in html and for passing it as JsonResponse

    :param user_obj: dict
    :return: dict
    """
    return {
        "id": user_obj.get("id"),
        "first_name": user_obj.get("first_name"),
        "last_name": user_obj.get("last_name"),
        "email": user_obj.get("email"),
        "username": user_obj.get("username"),
        "is_active": 1 if int(user_obj.get("is_active")) else 0,
    }


def delete_crud_user_object(id: int) -> dict:
    """
    delete user with specific id if exist else DoesNowExist error

    :param id: int
    :return: dict
    """
    obj = User.objects.get(id=id)
    obj.delete()


def update_user_data(user, data: dict):
    """
    update user data if the user exist

    :param user: queryset
    :param data: dict
    """
    user.first_name = data.get("first_name", user.first_name)
    user.last_name = data.get("last_name", user.last_name)
    user.email = data.get("email", user.email)
    user.is_active = data.get("is_active", user.is_active)
    user.save(update_fields=["first_name", "last_name", "email", "is_active"])
    return serialize_response_data(user.__dict__)
