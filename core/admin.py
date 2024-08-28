from django.contrib import admin
from core.models import CrudUser


@admin.register(CrudUser)
class CrudUserAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "status"]
    readonly_fields = ["id", "created", "modified"]
    fieldsets = (
        (
            "Personal Details",
            {"fields": ["id", "title", "description", "age"], "classes": "collapase"},
        ),
        (
            "Login & Status Details",
            {"fields": ["created", "modified", "status"], "classes": "collapase"},
        ),
    )
    search_fields = ["title"]
