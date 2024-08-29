from django.urls import path
from core.views import IndexView, InfoView, AddUser, DeleteUser
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("users", cache_page(0)(IndexView.as_view()), name="users"),
    path("add_user", AddUser.as_view(), name="add-user"),
    path("delete_user", DeleteUser.as_view(), name="delete-user"),
    path("info", InfoView.as_view(), name="info"),
]
