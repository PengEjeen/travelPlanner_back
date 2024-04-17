from django.db import models

# Create your models here.

class Cell(models.Model):   
    cell_id = models.CharField(max_length=20)
    cell_status = models.IntegerField(max_length=20)
    place_id = models.CharField(max_length=30)
    
        

