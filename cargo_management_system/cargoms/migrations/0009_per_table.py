# Generated by Django 3.0.3 on 2020-03-27 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargoms', '0008_auto_20200320_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='per_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per', models.IntegerField()),
                ('Description', models.CharField(max_length=20)),
            ],
        ),
    ]