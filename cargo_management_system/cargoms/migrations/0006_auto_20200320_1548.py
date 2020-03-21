# Generated by Django 3.0.3 on 2020-03-20 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargoms', '0005_auto_20200319_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee_Details',
            fields=[
                ('eid_no', models.IntegerField(primary_key=True, serialize=False)),
                ('e_name', models.CharField(max_length=45)),
                ('e_contact', models.IntegerField()),
                ('e_add', models.TextField()),
                ('e_mail', models.EmailField(max_length=254)),
                ('e_userName', models.CharField(max_length=45, unique=True)),
                ('e_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='employeeDetails',
        ),
    ]
