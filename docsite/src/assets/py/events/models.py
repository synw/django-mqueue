from django.db import models
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

class MyModel(models.Model):
    name = models.CharField(max_length=120)
    user = models.ForeignKey(
        USER_MODEL,
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    def get_event_object_url(self) -> str:
        return f"/some/url/{self.name}"
