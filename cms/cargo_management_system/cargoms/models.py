from django.db import models

# Create your models here.
class adminProfile(models.Model):
    name = models.CharField(max_length = 45)
    password = models.CharField(max_length = 45)
    permission_id = models.PositiveIntegerField()

    def __str__(self):
        return self.log_id

class employee_Details(models.Model):
    eid_no = models.CharField(max_length=5, primary_key = True)
    e_name = models.CharField(max_length = 45)
    e_contact = models.IntegerField()
    e_add = models.TextField()
    e_mail = models.EmailField()
    e_userName = models.CharField(max_length = 45 , unique = True)
    e_password = models.CharField(max_length = 50)

    def __str__(self):
        return self.eid_no , self.e_userName , self.e_name

class consignDetails(models.Model):
    c_id = models.IntegerField(primary_key = True )
    c_desc = models.TextField()
    c_quan = models.IntegerField()
    c_price = models.IntegerField()
    c_to = models.TextField()
    c_from = models.TextField()
    c_date = models.DateField()

    def __str__(self):
        return [self.c_id,self.c_desc, self.c_quan ,self.c_price , self.c_to ,self.c_from ,self.c_date]

class transcDetails(models.Model):
    t_id = models.IntegerField(primary_key = True)
    t_amt = models.IntegerField()
    t_date = models.DateField()

    def __str__(self):
        return self.t_id

class billDetails(models.Model):
    b_id = models.IntegerField(primary_key = True)
    b_desc = models.TextField()
    b_amt = models.IntegerField()
    b_ship = models.TextField()

    def __str__(self):
        return self.b_id , self.b_desc