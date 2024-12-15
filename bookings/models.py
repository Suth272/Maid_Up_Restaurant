
from django.db import models

# Model for tables
class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()

    def __str__(self):
        return f"Table {self.number} ({self.seats} seats)"

# Model for reservations
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"