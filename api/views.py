from  rest_framework import viewsets
from .serializer import SensorSerializer
from .models import Sensor
# Create your views here.

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class= SensorSerializer
