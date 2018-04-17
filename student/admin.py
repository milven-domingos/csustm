from django.contrib import admin

# Register your models here.
from student.forms import StudentForm
from student.models import Student


admin.site.register(Student)