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

class Controller(models.Model):
  name_controller=models.CharField(max_length=50)
  logical_controller=models.CharField(max_length=50)

class Transmission_medium(models.Model):
  name_transmission_medium=models.CharField(max_length=30)
  type_transmission_medium=models.CharField(max_length=50)

class Domotic_central(models.Model):
  name_domotic_central=models.CharField(max_length=20)
  interface_domotic_central=models.CharField(max_length=50)
  def __str__(self):
    #retorno el nombre de la central
    return self.name_domotic_central

class User(models.Model):
  name_user=models.CharField(max_length=30)
  password_user=models.CharField(max_length=20)  
  def __str__(self):
    # Retorno el nombre del usuario
    return self.name_user



class SensorActuator(models.Model):
  sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE) 
  actuator = models.ForeignKey(Actuator, on_delete=models.CASCADE)
  condition = models.CharField(max_length=50)

    # Definimos la clave primaria compuesta por los dos campos anteriores
class Meta:
  unique_together = (('sensor', 'actuator'),)


class ControllerSensor(models.Model):
  controller = models.ForeignKey(Controller, on_delete=models.CASCADE)
  sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)


class Meta:
  unique_together = (('controller', 'sensor'),)


class ControllerActuator(models.Model):
  controller = models.ForeignKey(Controller, on_delete=models.CASCADE)
  actuator = models.ForeignKey(Actuator, on_delete=models.CASCADE)

    # Definimos la clave primaria compuesta por los dos campos anteriores
class Meta:
  unique_together = (('controller', 'actuator'),)

class MediumController(models.Model):
    medium = models.ForeignKey(Transmission_medium, on_delete=models.CASCADE)
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE)

    # Definimos la clave primaria compuesta por los dos campos anteriores
class Meta:
  unique_together = (('medium', 'controller'),)

class CentralController(models.Model):
  central = models.ForeignKey(Domotic_central, on_delete=models.CASCADE)
  controller = models.ForeignKey(Controller, on_delete=models.CASCADE)

    # Definimos la clave primaria compuesta por los dos campos anteriores
class Meta:
  unique_together = (('central', 'controller'),)

class UserCentral(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_central')
  central = models.ForeignKey(Domotic_central, on_delete=models.CASCADE, related_name='name_central')
  permission = models.CharField(max_length=50) # Permiso que tiene el usuario sobre la central

    # Definimos la clave primaria compuesta por los dos campos anteriores
class Meta:
  unique_together = (('user', 'central'),)