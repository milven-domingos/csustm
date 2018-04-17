import datetime
from django.db import models

# Create your models here.
from department.models import SchoolDepartment


class Course(models.Model):
    name = models.CharField(max_length=60)
    duration = models.IntegerField()
    course_outline = models.TextField()
    #course_instructor = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(SchoolDepartment, on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
#
class Semester(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=60)
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    subject_outline = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class TextType(models.Model):
    name = models.CharField(max_length=155)
    percanteges = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class ClassName(models.Model):
    name = models.CharField(max_length=155, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)
    subjects = models.ManyToManyField(Subject)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
