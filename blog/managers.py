from datetime import datetime

from django.db import models


class EventManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

    def public(self):
        return self.get_queryset().filter(is_displayed=True)

    def future(self):
        return self.public().filter(to_date__gte=datetime.now()).order_by("from_date")

    def past(self):
        return self.public().filter(to_date__lte=datetime.now()).order_by("-to_date")
