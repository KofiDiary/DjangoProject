from django.db import models

# Create your models here.
class warehouse(models.Model):
    Warehouse_Number = models.PositiveIntegerField()
    Product_Name = models.CharField(max_length=200)
    Product_Quantity = models.CharField(max_length=200)
    Product_State = models.CharField(max_length=200)
    Date_Added = models.DateTimeField()