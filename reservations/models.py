from django.db import models
from core import models as core_models


class Reservation(core_models.TimeStampedModel):
    """ Reservaion Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCEL = "cancel"
    STATUS_CHOICES = (
        (STATUS_PENDING, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCEL, "cancel"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING)
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
    check_in = models.DateField()
    chech_out = models.DateField()

    def __str__(self):
        return f'{self.room} - {self.check_in}'
