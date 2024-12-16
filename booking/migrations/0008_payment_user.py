# Generated by Django 5.0.6 on 2024-07-31 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_bookingservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_payment', to='booking.user'),
            preserve_default=False,
        ),
    ]
