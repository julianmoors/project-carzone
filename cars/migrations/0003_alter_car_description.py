# Generated by Django 5.0.4 on 2024-04-15 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_features_alter_car_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
