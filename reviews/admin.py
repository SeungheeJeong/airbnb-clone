from django.contrib import admin
from . import models


@admin.register(models.Review)
class Review(admin.ModelAdmin):
    """Review Admin Definition"""
    list_display = (
        "review",
        "Accuracy",
        "communication",
        "cleanliness",
        "location",
        "check_in",
        "value",
        "user",
        "room"
    )

    
