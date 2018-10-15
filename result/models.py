from django.db import models

# Create your models here.

class ResultInfo(models.Model):
    std_name = models.CharField(max_length=30)
    std_class = models.IntegerField()
    std_roll = models.IntegerField()
    subject = models.CharField(max_length=30)
    mark = models.IntegerField()


    def __str__(self):
        return self.std_name