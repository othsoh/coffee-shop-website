from django.utils    import timezone
from django.db import models
from django.contrib.auth import get_user_model
from users.models import Profile
import datetime



# Create your models here.


User= get_user_model()

from django.db import models


class Reservation(models.Model):
    Type_Choices=[
        ("table","table"),
        ("etudiant","etudiant"),
        ("billard","billard"),
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    date=models.DateTimeField(null=True,blank=True, )
    time = models.TimeField(null=True,blank=True)
    num_guests = models.PositiveIntegerField(default=1)
    reservation_type = models.CharField(max_length=200, choices=Type_Choices, default="table")

    
    def remaining_time(self):
        now = timezone.now()
        reservation_datetime = timezone.make_aware(datetime.datetime.combine(self.date, self.time))
        remaining_time = reservation_datetime - now

        days = remaining_time.days
        
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, remainder = divmod(remainder, 60)

        remaining_str = f"{days} days, {hours} hours, {minutes} minutes"
        return remaining_str


    def __str__(self):
        return str(self.user)
