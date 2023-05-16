# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import TemperatureMeasurement
from rest_framework.response  import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,UpdateAPIView,RetrieveUpdateAPIView,RetrieveAPIView,CreateAPIView
from .models import Sensor
from .serializers import SensorChangeSerializer, SensorSerialazer, TemperatureMeasurementSerialazer

class GetSensor(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialazer


class CreateSensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialazer
  
    
class UpdateSensor(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialazer


class Add_Temperature_Sensor(ListCreateAPIView):
    queryset = TemperatureMeasurement.objects.all()
    serializer_class = TemperatureMeasurementSerialazer

# class Add_Temperature_Sensor(UpdateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorChangeSerializer

class GetSensorInformation(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialazer
