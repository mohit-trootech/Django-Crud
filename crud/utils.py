from core.models import CrudUser


def create_crud_user_object(data: dict):
    obj = CrudUser.objects.create(
        title=data.get("title"),
        age=int(data.get("age")),
    )
    return obj.__dict__
