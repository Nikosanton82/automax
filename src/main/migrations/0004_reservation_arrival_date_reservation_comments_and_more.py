# Generated by Django 4.1.7 on 2023-03-19 12:45

from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_reservation_arrival_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='arrival_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reservation',
            name='comments',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='departure_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reservation',
            name='hotel_name',
            field=models.CharField(default='artemis', max_length=255),
        ),
        migrations.AddField(
            model_name='reservation',
            name='language',
            field=models.CharField(default='**', max_length=2),
        ),
        migrations.AddField(
            model_name='reservation',
            name='mobile_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+1 ', max_length=20, region=None),
        ),
        migrations.AddField(
            model_name='reservation',
            name='num_adults',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reservation',
            name='num_children_0_4',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='num_children_5_12',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='tours',
            field=models.TextField(default=''),
        ),
    ]
