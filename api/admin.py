from django.contrib import admin
from .models import Sensor,Actuator,SensorActuator, ControllerSensor, ControllerActuator, MediumController, CentralController, UserCentral

admin.site.register(Sensor)
admin.site.register(Actuator)
admin.site.register(SensorActuator)
admin.site.register(ControllerSensor)
admin.site.register(ControllerActuator)
admin.site.register(MediumController)
admin.site.register(CentralController)
admin.site.register(UserCentral)