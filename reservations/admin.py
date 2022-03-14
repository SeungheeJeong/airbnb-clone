from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class Reservation(admin.ModelAdmin):
    """Review Admin Definition"""
    list_display = (
        "status",
        "room",
        "guest",
        "chech_out",
        "check_in"

    )
