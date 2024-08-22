from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = models.Manager()

class Program(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    objects = models.Manager()

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    objects = models.Manager()

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    YEAR_CHOICES = (
        ("Level 1", "Level 1"),
        ("Level 2", "Level 2"),
        ("Level 3", "Level 3"),
        ("Level 4", "Level 4"),
        ("Level 5", "Level 5"),
        ("Spillover 1", "Spillover 1"),
        ("Spillover 2", "Spillover 2")
    )
    year = models.CharField(max_length=255, choices=YEAR_CHOICES)
    courses = models.ManyToManyField(Course)
    objects = models.Manager()