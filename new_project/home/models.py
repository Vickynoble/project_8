from django.db import models

# Create your models here.
class Hotel_records(models.Model):
    occupant_first_name = models.CharField(max_length=50)
    occupant_last_name = models.CharField(max_length=50)
    occupant_occupation = models.CharField(max_length=50)
    occupant_email = models.EmailField(null=True, blank=True)
    room_number = models.CharField(max_length=20)
    amount_paid = models.FloatField()
    number_of_night = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.occupant_first_name} {self.room_number}'

