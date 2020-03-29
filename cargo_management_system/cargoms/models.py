from django.db import models

# Create your models here.

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

class per_table(models.Model):
    per = models.IntegerField()
    Description = models.CharField(max_length=30)    