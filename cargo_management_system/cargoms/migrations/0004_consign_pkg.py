# Generated by Django 3.0.3 on 2020-04-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargoms', '0003_auto_20200413_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='consign_pkg',
            fields=[
                ('c_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('order_id', models.IntegerField()),
                ('pkg_r_date', models.DateField()),
                ('d_sh_date', models.DateField()),
            ],
        ),
    ]
