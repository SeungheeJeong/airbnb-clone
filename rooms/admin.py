from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    fieldsets = (
        ("Basic Info",
         {"fields": ("name",
                     "description",
                     "country",
                     "city",
                     "price")},
         ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
            "Spaces",
            {"fields": (
                "guests",
                "beds",
                "bedrooms",
                "baths"
            )},
        ),
        (
            "More About the Space",
            {"fields": (
                "amenities", "facilities", "house_rules"
            )},
        ),
        (
            "Last Details",
            {"fields": (
                "host",
            )},
        ),
    )
    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    filter_horizontal = ["amenities", "facilities", "house_rules", ]

    list_filter = (
        "instant_book", "city", "country"
    )

    search_fields = (
        "^city", "^host__username"
    )  # None - icontain: 완성되지 않은 문자로도 검사 / ^startswich 를 추가하면 완성된 문자로 검사


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""
    pass
