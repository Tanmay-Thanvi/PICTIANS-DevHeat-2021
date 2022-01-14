from django.db import models

class Level(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    lvlno = models.IntegerField()
    num = models.IntegerField()
    time = models.CharField(max_length=100)

class Exercise(models.Model):
    catid = models.IntegerField()
    name = models.CharField(max_length=100)
    count = models.IntegerField()