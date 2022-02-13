from django.db import models


GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)
DEPT_CHOICES = (
    (0, 'cse'),
    (1, 'ece')
)

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=64)
    #username = models.CharField(max_length=64)
    mis = models.IntegerField(primary_key=True,blank=False)
    date_of_birth = models.DateField()
    gender = models.IntegerField(choices=GENDER_CHOICES, default = 2)# models.
    gpa = models.FloatField(default=0.0)
    stream = models.IntegerField(choices=DEPT_CHOICES, default=0)
    # address = models.TextField(max_length=200, default="Address")
    email = models.EmailField(unique=True, default="example@email.com")
    mobile_number = models.IntegerField(default=000000000)
    alternate_number = models.IntegerField(default=000000000)
    # profile_pictures = models.

    def __str__(self):
        return f"{self.mis} : {self.name}"