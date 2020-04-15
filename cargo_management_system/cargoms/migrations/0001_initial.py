# Generated by Django 3.0.3 on 2020-04-10 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='billDetails',
            fields=[
                ('b_id', models.IntegerField(primary_key=True, serialize=False)),
                ('b_desc', models.TextField()),
                ('b_amt', models.IntegerField()),
                ('b_ship', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='consignDetails',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField()),
                ('c_desc', models.TextField()),
                ('c_quan', models.IntegerField()),
                ('c_price', models.IntegerField()),
                ('c_to', models.TextField()),
                ('c_from', models.TextField()),
                ('c_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='cust_details',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=50)),
                ('s_contact', models.CharField(max_length=10)),
                ('s_add', models.CharField(max_length=100)),
                ('s_city', models.CharField(max_length=30)),
                ('s_state', models.CharField(max_length=30)),
                ('s_pincode', models.IntegerField()),
                ('r_name', models.CharField(max_length=45)),
                ('r_contact', models.CharField(max_length=10)),
                ('r_add', models.CharField(max_length=100)),
                ('r_city', models.CharField(max_length=30)),
                ('r_state', models.CharField(max_length=30)),
                ('r_pincode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='cust_pkg_details',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('s_i_no', models.IntegerField()),
                ('cust_name', models.CharField(max_length=45)),
                ('pkg_r_date', models.DateField()),
                ('pkg_r_time', models.TimeField()),
                ('pkg_d_date', models.DateField()),
                ('pkg_d_time', models.TimeField()),
                ('pkg_weight', models.IntegerField()),
                ('pkg_ship_add', models.TextField()),
                ('pkg_ship_city', models.CharField(max_length=45)),
                ('pkg_ship_pincode', models.IntegerField()),
                ('ship_service_type', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='employee_Details',
            fields=[
                ('eid_no', models.IntegerField(primary_key=True, serialize=False)),
                ('e_name', models.CharField(max_length=45)),
                ('e_contact', models.CharField(max_length=10)),
                ('e_add', models.TextField()),
                ('e_mail', models.EmailField(max_length=254)),
                ('e_per_id', models.CharField(max_length=6)),
                ('e_userName', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='per_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per', models.IntegerField()),
                ('Description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='transc_Details',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=50)),
                ('t_amt', models.IntegerField()),
                ('t_date', models.DateField()),
                ('t_time', models.TimeField()),
            ],
        ),
    ]
