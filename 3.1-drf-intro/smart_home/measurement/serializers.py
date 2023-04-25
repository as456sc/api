from .models import Sensor
from .models import TemperatureMeasurement
from rest_framework import serializers

# TODO: опишите необходимые сериализаторы


class TemperatureMeasurementSerialazer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureMeasurement
        fields = ['temparature_measurements','date_time_now_add_measurements']
        # fields = ['temparature_measurements','date_time_now_measurements']

class SensorSerialazer(serializers.ModelSerializer):
    measurements = TemperatureMeasurementSerialazer(read_only =True, many = True)


    class Meta:
        model = Sensor
        fields = ['id','title','description','measurements']