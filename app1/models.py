from django.db import models


class Teacher(models.Model):
    tname = models.CharField(max_length=20)
    tage = models.IntegerField()
    tgender = models.CharField(max_length=2)
    
    def __str__(self):
        return self.tname


class Student(models.Model):
    sname = models.CharField(max_length=20)
    sage = models.IntegerField()
    sgender = models.CharField(max_length=2)
    s_t = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.sname
