# Generated by Django 3.0.3 on 2020-06-06 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='consign_Details',
            fields=[
                ('p_id', models.IntegerField(primary_key=True, serialize=False)),
                ('c_id', models.CharField(max_length=20)),
                ('c_desc', models.TextField()),
                ('c_quan', models.IntegerField()),
                ('c_to', models.TextField()),
                ('c_from', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='consign_pkg',
            fields=[
                ('c_id', models.CharField(max_length=20)),
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
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
                ('cust_name', models.CharField(max_length=45)),
                ('s_i_no', models.IntegerField()),
                ('pkg_r_date', models.DateField()),
                ('pkg_r_time', models.TimeField()),
                ('pkg_d_date', models.DateField()),
                ('pkg_d_time', models.TimeField()),
                ('quantity', models.IntegerField()),
                ('pkg_rate_p_piece', models.IntegerField()),
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
            name='state_code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=30)),
                ('state_code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='t_o_delivery',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('c_from', models.TextField()),
                ('c_to', models.TextField()),
                ('d_date', models.DateTimeField()),
                ('d_sh_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='temp_pkg_model',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=50)),
                ('r_city', models.CharField(max_length=30)),
                ('r_state', models.CharField(max_length=30)),
                ('pkg_r_date', models.DateField()),
                ('pkg_weight', models.IntegerField()),
                ('pkg_quantity', models.IntegerField()),
                ('pkg_rate_p_piece', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='transc_Details',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('pkg_rate_p_piece', models.IntegerField()),
                ('t_amt', models.IntegerField()),
                ('t_date', models.DateField()),
                ('t_time', models.TimeField()),
            ],
        ),
    ]
