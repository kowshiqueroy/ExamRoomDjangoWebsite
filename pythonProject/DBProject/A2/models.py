from django.db import models

# Create your models here.





class Link(models.Model):
   institute = models.CharField(max_length=100, default="")
   dept = models.CharField(max_length=100, default="")
   course = models.CharField(max_length=100, default="")
   password = models.CharField(max_length=100, default="")