
from django.db import models

# Model for tables
class Table(models.Model):
    number = models.IntegerField(unique=True) # Unique table number
    seats = models.IntegerField() # Number of seats available at the table

    def __str__(self):
        return f"Table {self.number} ({self.seats} seats)"

# Model for reservations
class Reservation(models.Model):
    name = models.CharField(max_length=100) # Customer's name
    email = models.EmailField() # Customer's email
    phone = models.CharField(max_length=15) # Customer's phone number
    table = models.ForeignKey(Table, on_delete=models.CASCADE) # Table assigned to the reservation
    date = models.DateField() # Date of the reservation
    time = models.TimeField() # Time of the reservation
    guests = models.IntegerField()  # Number of guests


    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"