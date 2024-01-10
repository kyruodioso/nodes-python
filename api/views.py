from rest_framework import viewsets

from .serializer import UserSerializer, Domotic_centralSerializer, SensorSerializer, ActuatorSerializer, SensorActuatorSerializer, ControllerSensorSerializer, ControllerActuatorSerializer, MediumControllerSerializer, CentralControllerSerializer, UserCentralSerializer

from .models import User, Domotic_central,Sensor, Actuator, SensorActuator, ControllerSensor, ControllerActuator, MediumController, CentralController, UserCentral

class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class= UserSerializer

class DomoticCentralViewSet(viewsets.ModelViewSet):
    queryset=Domotic_central.objects.all()
    serializer_class=Domotic_centralSerializer
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class ActuatorViewSet(viewsets.ModelViewSet):
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer

class SensorActuatorViewSet(viewsets.ModelViewSet):
    queryset = SensorActuator.objects.all()
    serializer_class = SensorActuatorSerializer

class ControllerSensorViewSet(viewsets.ModelViewSet):
    queryset = ControllerSensor.objects.all()
    serializer_class = ControllerSensorSerializer

class ControllerActuatorViewSet(viewsets.ModelViewSet):
    queryset = ControllerActuator.objects.all()
    serializer_class = ControllerActuatorSerializer

class MediumControllerViewSet(viewsets.ModelViewSet):
    queryset = MediumController.objects.all()
    serializer_class = MediumControllerSerializer

class CentralControllerViewSet(viewsets.ModelViewSet):
    queryset = CentralController.objects.all()
    serializer_class = CentralControllerSerializer

class UserCentralViewSet(viewsets.ModelViewSet):
    queryset = UserCentral.objects.all()
    serializer_class = UserCentralSerializer