from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    title = models.CharField(max_length=200, verbose_name= 'Датчик')
    description = models.CharField(max_length=200, verbose_name= 'Описание')

class TemperatureMeasurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name= 'measurements')

    temparature_measurements = models.FloatField(verbose_name= 'Температура')
    date_time_now_add_measurements = models.DateTimeField(auto_now_add=True, verbose_name= 'Время')