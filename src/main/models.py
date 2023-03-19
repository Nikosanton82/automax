import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = PhoneNumberField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email} - {self.phone_number}"
