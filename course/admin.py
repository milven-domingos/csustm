from django.contrib import admin

# Register your models here.
from course.models import *

admin.site.register(Course)
admin.site.register(ClassName)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(TextType)