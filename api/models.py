from django.db import models

# Create your models here.
class Sensor(models.Model):
  name_sensor= models.CharField(max_length=50)
  type_sensor= models.CharField(max_length=50)
  value_sensor= models.FloatField()
  ubication_sensor= models.CharField(max_length=50)
  is_active= models.BooleanField(default=False)