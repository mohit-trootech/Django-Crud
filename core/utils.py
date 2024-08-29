from django.contrib.auth.models import User
from crud.constant import STATUS_204, STATUS_404, UNIQUE_USER_ERROR
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


def serialize_response_data(user_obj):
    return {
        "id": user_obj.get("id"),
        "first_name": user_obj.get("first_name"),
        "last_name": user_obj.get("last_name"),
        "email": user_obj.get("email"),
        "username": user_obj.get("username"),
        "is_active": "Active" if user_obj.get("is_active") else "Unactive",
    }


def delete_crud_user_object(id: int):
    try:
        obj = User.objects.get(id=id)
        obj.delete()
        return {"status": STATUS_204}
    except User.DoesNotExist:
        return {"status": STATUS_404}
