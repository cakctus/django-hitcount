from django.db import models
from hitcount.models import HitCountMixin


class HitCount(models.Model, HitCountMixin):

    endpoint = models.CharField(max_length=255000000000000000)
    hits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.endpoint
