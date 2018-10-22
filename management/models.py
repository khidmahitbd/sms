from django.db import models

# Create your models here.
class StudentClass(models.Model):

    class_name = models.CharField(max_length = 7)


    def __str__(self):
        return self.class_name


class Subject(models.Model):

    
    subject = models.CharField(max_length = 30)
    class_name = models.ForeignKey(StudentClass,on_delete= models.CASCADE)
    
    
    def __str__(self):
        return self.subject
