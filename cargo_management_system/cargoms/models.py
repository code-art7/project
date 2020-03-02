from django.db import models

# Create your models here.
class admin_login(models.Model):
    log_id = models.CharField(unique=True, max_length = 45)
    name = models.CharField(max_length = 45)
    password = models.CharField(max_length = 45)
    permission_id = models.PositiveIntegerField()

    def __str__(self):
        return self.log_id