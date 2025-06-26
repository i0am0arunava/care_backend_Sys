from django.db import models

from care.utils.models.base import BaseModel


class EMRBaseModel(BaseModel):
    history = models.JSONField(default=dict)
    meta = models.JSONField(default=dict)
    created_by = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        default=None,
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_created_by",
    )
    updated_by = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        default=None,
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_updated_by",
    )

    class Meta:
        abstract = True
