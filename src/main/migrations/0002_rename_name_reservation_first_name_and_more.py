# Generated by Django 4.1.7 on 2023-03-19 06:44

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('de', 'German'), ('fr', 'French'), ('ru', 'Russian'), ('it', 'Italian'), ('pl', 'Polish'), ('cs', 'Czechish')], max_length=2),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='mobile_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]