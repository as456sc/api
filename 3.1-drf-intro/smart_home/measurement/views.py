# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import TemperatureMeasurement
from rest_framework.response  import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,UpdateAPIView,RetrieveUpdateAPIView,RetrieveAPIView,CreateAPIView
from .models import Sensor
from .serializers import  SensorSerialazer, TemperatureMeasurementSerialazer,SensorListSerializer

class GetSensor(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class CreateSensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialazer
  
    
class UpdateSensor(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialazer


class Add_Temperature_Sensor(ListCreateAPIView):
    queryset = TemperatureMeasurement.objects.all()
    serializer_class = TemperatureMeasurementSerialazer



class GetSensorInformation(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialazer
