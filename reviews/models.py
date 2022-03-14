from django.db import models
from core import models as core_models
# Create your models here.


class Review(core_models.TimeStampedModel):
    """Review Model Definition"""

    review = models.TextField()
    Accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    # model에서 문자열 출력해주고 싶을 때 사용
    # def __str__(self):
    #     return f'{self.room} - {self.check_in}'
