from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField(upload_to="img")
    lesson_count = models.IntegerField(default=0)
class User(models.Model):
    nickname = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    plan = models.ForeignKey(to=Plan,on_delete=models.CASCADE)
class Lesson(models.Model):
    lable = models.CharField(max_length=32)
    picture = models.ImageField(upload_to="img")
    show_number = models.IntegerField()
    plan = models.ManyToManyField(to=Plan,)
# Create your models here.

























