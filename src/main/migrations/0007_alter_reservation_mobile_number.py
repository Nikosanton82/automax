# Generated by Django 4.1.7 on 2023-03-19 18:26

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_reservation_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='mobile_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
