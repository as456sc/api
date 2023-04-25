from django.urls import path
from measurement.views import GetSensor,CreateSensor,UpdateSensor,GetSensorInformation,Add_Temperature_Sensor

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/',GetSensor.as_view()),
    path('sensors_create/',CreateSensor.as_view()),
    path('sensors_upp/<pk>/',UpdateSensor.as_view()),
    path('measurements/<pk>/',Add_Temperature_Sensor.as_view()),
    path('sensors_get/<pk>/',GetSensorInformation.as_view())
]


