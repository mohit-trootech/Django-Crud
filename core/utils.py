from core.models import CrudUser
from crud.constant import (
    STATUS_200,
    USER_DELETE_SUCCESS,
    STATUS_404,
    USER_DELETE_404,
)


def create_crud_user_object(data: dict):
    obj = CrudUser.objects.create(
        title=data.get("title"),
        age=int(data.get("age")),
    )
    return obj.__dict__


def delete_crud_user_object(id: int):
    print(id)
    try:
        obj = CrudUser.objects.get(id=id)
        obj.delete()
        return {"status": STATUS_200, "content": USER_DELETE_SUCCESS}
    except CrudUser.DoesNotExist:
        return {"status": STATUS_404, "content": USER_DELETE_404.format(id=id)}
