from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models
# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """abstract items"""
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """Room Type Object Definition """
    class Meta:
        verbose_name = "Room Type"  # Admin Panel 에 보이는 이름 설정
        ordering = ['name']


class Amenity(AbstractItem):
    """Amenity Object Definition """
    class Meta:
        verbose_name = "Amenitie"


class Facility(AbstractItem):
    """Facility Object Definition """
    class Meta:
        verbose_name = "Facilitie"


class HouseRule(AbstractItem):
    """HouseRule Object Definition """
    pass


class Room(core_models.TimeStampedModel):
    """Room Model Definition"""
    name = models.CharField(max_length=140)
    description = models.TextField(default="")
    country = CountryField(blank_label='(select country)', blank=True)
    city = models.CharField(max_length=80, default="")
    price = models.IntegerField()  # 소수점은 DecimalField
    address = models.CharField(max_length=140, blank=True)
    guests = models.IntegerField(default=1)
    beds = models.IntegerField(default=1)
    bedrooms = models.IntegerField(default=1)
    baths = models.IntegerField(default=1)
    check_in = models.TimeField(blank=True, default="")
    check_out = models.TimeField(blank=True, default="")
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        user_models.User, related_name="rooms", on_delete=models.CASCADE)
    room_type = models.ForeignKey(
        RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(
        "Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField(
        Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(
        HouseRule, related_name="rooms", blank=True)

    def __str__(self):
        # ROOM 타이틀을 name으로 전달하기 위한 것
        return self.name


class Photo(core_models.TimeStampedModel):
    """Photo Model Definition"""
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
