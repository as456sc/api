from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class TemperatureMeasurement(models.Model):
    temparature_measurements = models.FloatField()
    # date_time_now_measurements = models.DateTimeField(auto_now=True)
    date_time_now_add_measurements = models.DateTimeField(auto_now_add=True)