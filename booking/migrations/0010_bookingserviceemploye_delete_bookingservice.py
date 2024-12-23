# Generated by Django 5.0.6 on 2024-07-31 19:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_room_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingServiceEmploye',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.booking')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.employe')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.user')),
            ],
            options={
                'verbose_name': 'BookingService',
                'verbose_name_plural': 'BookingServices',
                'ordering': ['booking'],
            },
        ),
        migrations.DeleteModel(
            name='BookingService',
        ),
    ]
