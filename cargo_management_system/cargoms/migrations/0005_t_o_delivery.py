# Generated by Django 3.0.3 on 2020-06-12 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargoms', '0004_delete_t_o_delivery'),
    ]

    operations = [
        migrations.CreateModel(
            name='t_o_delivery',
            fields=[
                ('c_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('c_to', models.TextField()),
                ('d_date', models.DateTimeField()),
            ],
        ),
    ]
