# Generated by Django 4.1.7 on 2023-03-19 16:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_reservation_arrival_date_reservation_comments_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='arrival_date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='departure_date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='hotel_name',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='language',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='num_adults',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='num_children_0_4',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='num_children_5_12',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='tours',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
