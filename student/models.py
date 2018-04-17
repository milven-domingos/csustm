import datetime
from django.db import models
from django.conf import settings
# Create your models here.
from course.models import Course, Subject, ClassName
from csustm.file_validation import ContentTypeRestrictedFileField, get_upload_image

DOC_TYPE = (
    ('Passaporte', 'Passaporte'),
    ('Carta de Conducao', 'Carta de Conducao'),
    ('BI', 'BI'),
    ('DIRE', 'DIRE'),
)


class Student(models.Model):
    profile_photo = ContentTypeRestrictedFileField(upload_to=get_upload_image, default="none.jpg",
    content_types=['image/png','image/jpeg','image/jpg'], max_upload_size=4242880, blank=True)
    quotes = models.CharField(blank=True,max_length=155)
    bio = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(default=datetime.datetime.now)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)
    student_account = models.OneToOneField(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE,
                                        related_name='students', related_query_name='student')


class StudentClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_class = models.ForeignKey(ClassName, on_delete=models.CASCADE,blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(default=datetime.datetime.now)
    def __str__(self):
        return self.student

class StudentMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_name = models.ForeignKey(ClassName, on_delete=models.CASCADE,blank=True, null=True)
    mark = models.FloatField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(default=datetime.datetime.now)
    def __str__(self):
        return self.student
