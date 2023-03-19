import uuid
from django.db import models


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20, default='123456789')  # max_length for phone numbers is typically around 20

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
