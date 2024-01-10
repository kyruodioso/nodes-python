from rest_framework import serializers

from .models import Sensor, Actuator, SensorActuator, ControllerSensor, ControllerActuator, MediumController, CentralController, UserCentral, User, Domotic_central

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Domotic_centralSerializer(serializers.ModelSerializer):
    class Meta:
        model=Domotic_central
        fields = '__all__'
class SensorActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorActuator
        fields = '__all__'

class ControllerSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControllerSensor
        fields = '__all__'

class ControllerActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControllerActuator
        fields = '__all__'

class MediumControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediumController
        fields = '__all__'

class CentralControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralController
        fields = '__all__'

class UserCentralSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCentral
        fields = '__all__'
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sensor
        fields= '__all__'

class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Actuator
        fields= '__all__'