from django.db import models

########### PERMISSION ###############
class per_table(models.Model):
    per = models.IntegerField()
    Description = models.CharField(max_length=30)    

########### EMPLOYEE DETAILS ###############
class employee_Details(models.Model):
    eid_no = models.IntegerField(primary_key = True)
    e_name = models.CharField(max_length = 45)
    e_contact = models.CharField(max_length=10)
    e_add = models.TextField()
    e_mail = models.EmailField()
    e_per_id = models.CharField(max_length=6)
    e_userName = models.CharField(max_length = 45 , unique = True)

    def __str__(self):
        return self.eid_no , self.e_userName , self.e_name


########### CUSTOMER MODULE ################
class cust_details(models.Model):
    order_id = models.IntegerField(primary_key=True)
    cust_name = models.CharField( max_length=50)
    s_contact = models.CharField(max_length=10)
    s_add = models.CharField(max_length=100)
    s_city = models.CharField(max_length=30)
    s_state = models.CharField(max_length=30)
    s_pincode = models.IntegerField()

    r_name = models.CharField(max_length=45)
    r_contact = models.CharField(max_length=10)
    r_add = models.CharField(max_length=100)
    r_city = models.CharField(max_length=30)
    r_state = models.CharField(max_length=30)
    r_pincode = models.IntegerField()
    
class cust_pkg_details(models.Model):
    order_id = models.IntegerField(primary_key=True)
    s_i_no = models.IntegerField()
    cust_name = models.CharField(max_length=45)
    pkg_r_date = models.DateField()
    pkg_r_time = models.TimeField()
    pkg_d_date = models.DateField()
    pkg_d_time = models.TimeField()
    pkg_weight = models.IntegerField()
    pkg_ship_add = models.TextField()
    pkg_ship_city = models.CharField(max_length=45)
    pkg_ship_pincode = models.IntegerField()
    ship_service_type = models.CharField(max_length=45)

    def __str__(self):
        return self.order_id

########## TRANSACTION MODULE ###############
class transc_Details(models.Model):
    order_id = models.IntegerField(primary_key=True)
    cust_name = models.CharField( max_length=50)
    t_amt = models.IntegerField()
    t_date = models.DateField()
    t_time = models.TimeField()

    def __str__(self):
        return self.order_id

########### CARGO MODULE #############
class consignDetails(models.Model):
    c_id = models.IntegerField(primary_key = True )
    c_desc = models.TextField()
    c_quan = models.IntegerField()
    c_to = models.TextField()
    c_from = models.TextField()

    def __str__(self):
        return [self.c_id ]
    
class consign_pkg(models.Model):
    c_id = models.CharField(primary_key = True, max_length=20 )
    s_no = models.IntegerField()
    order_id = models.IntegerField()
    pkg_r_date = models.DateField()
    d_sh_date = models.DateField()

    def __str__(self):
        return [self.c_id ]

############ TIME OF DELIVERY MODULE ##############
class t_o_delivery(models.Model):
    c_id = models.IntegerField(primary_key = True )
    c_from = models.TextField()
    c_to = models.TextField()
    d_date = models.DateTimeField()
    d_sh_date = models.DateField()

    def __str__(self):
        return [self.c_id ]

