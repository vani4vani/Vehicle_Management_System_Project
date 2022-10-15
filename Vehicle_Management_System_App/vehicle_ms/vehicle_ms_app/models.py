from django.db import models
# datetime import datetime

# Create your models here.

VEHICLE_WHEELS = (
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)

class VehicleModel(models.Model):
    # Field Names
    vehicle_number = models.CharField(('name'), max_length=50, null=False, blank=False)
    vehicle_type = models.CharField(max_length = 20, choices = VEHICLE_WHEELS, default = '2')
    vehicle_model = models.CharField('Model', max_length=100)
    vehicle_description = models.TextField(verbose_name="Description about the vehicle.")
    #created_on = models.DateTimeField(default=datetime.now)
    
    
    # rename the instances of the model
    # with their title name
    def __str__(self) -> str:
         return self.vehicle_number