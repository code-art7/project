# Generated by Django 3.0.3 on 2020-06-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargoms', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='consign_pkg',
        ),
        migrations.RemoveField(
            model_name='consign_details',
            name='c_desc',
        ),
        migrations.AddField(
            model_name='consign_details',
            name='order_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]