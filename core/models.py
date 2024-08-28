from django_extensions.db.models import (
    TitleDescriptionModel,
    TimeStampedModel,
    ActivatorModel,
)
from django.db.models import IntegerField


class CrudUser(TitleDescriptionModel, TimeStampedModel, ActivatorModel):
    age = IntegerField()

    class Meta:
        ordering = ["-created"]
