from django.db import models

class Sections(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.ForeignKey(Sections,on_delete=models.CASCADE,null=True,blank=True)
    age = models.IntegerField()
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    mobileno = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    pic = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
