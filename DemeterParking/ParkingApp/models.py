from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """Profile Details of User (1:1 User)"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.DecimalField(decimal_places=2)
class Lot(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    rate = models.DecimalField(decimal_places=2)
    address = models.CharField()
    city = models.CharField()
    state = models.CharField(max_length=2)
    notes = models.TextField()
    postal = models.IntegerField(max_length=5)
    #False = Available
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.name
