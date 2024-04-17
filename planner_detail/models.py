from django.db import models

# Create your models here.
        
class Planner(models.Model):
    user_id = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    cells = models.JSONField(blank=True,
                             null=True)
    planner_id = models.CharField(max_length=20)
    dateTimeOfUpload = models.DateTimeField(auto_now=True)



