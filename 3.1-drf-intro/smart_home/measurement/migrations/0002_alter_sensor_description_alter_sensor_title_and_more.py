# Generated by Django 4.1.7 on 2023-05-20 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Датчик'),
        ),
        migrations.AlterField(
            model_name='temperaturemeasurement',
            name='date_time_now_add_measurements',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='temperaturemeasurement',
            name='sensor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor'),
        ),
        migrations.AlterField(
            model_name='temperaturemeasurement',
            name='temparature_measurements',
            field=models.FloatField(verbose_name='Температура'),
        ),
    ]
