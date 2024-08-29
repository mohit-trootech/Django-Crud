from django.urls import path
from core.views import IndexView, InfoView, HandleUser
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("users", cache_page(0)(IndexView.as_view()), name="users"),
    path("users_handle/<int:id>", HandleUser.as_view(), name="users-handle"),
    path("info", InfoView.as_view(), name="info"),
]
