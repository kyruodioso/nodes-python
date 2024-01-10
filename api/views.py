from  rest_framework import viewsets
from .serializer import SensorSerializer , ActuatorSerializer
from .models import Sensor , Actuator
# Create your views here.

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class= SensorSerializer

class ActuatorViewSet(viewsets.ModelViewSet):
    queryset = Actuator.objects.all()
    serializer_class= ActuatorSerializer
