from django.db import models

# Create your models here.

class Student(models.Model):
    id= models.IntegerField(primary_key=True)
    name= models.CharField(max_length=200)
    dob = models.DateField()
    email= models.EmailField(max_length = 254, default="default@example.com")
    course= models.CharField(max_length=50)
    cgpa= models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.id


