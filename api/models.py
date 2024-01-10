from django.db import models

# Create your models here.
class Sensor(models.Model):
  name_sensor= models.CharField(max_length=50)
  type_sensor= models.CharField(max_length=50)
  value_sensor= models.FloatField()
  ubication_sensor= models.CharField(max_length=50)
  is_active= models.BooleanField(default=False)

class Actuator(models.Model):
  name_actuator=models.CharField(max_length=50)
  type_actuator=models.CharField(max_length=50)
  value_actuator=models.BooleanField(default=False)
  is_active=models.BooleanField(default=False)
  ubication_actuator=models.CharField(max_length=50)