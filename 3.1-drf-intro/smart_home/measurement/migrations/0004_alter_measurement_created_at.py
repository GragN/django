# Generated by Django 4.0.4 on 2022-05-12 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_sensor_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
