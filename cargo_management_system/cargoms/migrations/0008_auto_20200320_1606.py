# Generated by Django 3.0.3 on 2020-03-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargoms', '0007_auto_20200320_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_details',
            name='e_contact',
            field=models.CharField(max_length=10),
        ),
    ]