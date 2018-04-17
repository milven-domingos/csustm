import datetime
from django.db import models

# Create your models here.
from django.conf import settings

from course.models import ClassName, Subject
from csustm.file_validation import ContentTypeRestrictedFileField, get_upload_image

DOC_TYPE = (
    ('Passaporte', 'Passaporte'),
    ('Carta de Conducao', 'Carta de Conducao'),
    ('BI', 'BI'),
    ('DIRE', 'DIRE'),
)

class Teacher(models.Model):
    profile_photo = ContentTypeRestrictedFileField(upload_to=get_upload_image, default="none.jpg",
    content_types=['image/png','image/jpeg','image/jpg'], max_upload_size=4242880, blank=True,null=True)
    quotes = models.CharField(blank=True,max_length=155)
    bio = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(default=datetime.datetime.now)
    degree = models.CharField(max_length=155)
    teacher_account = models.OneToOneField(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE,
                                        related_name='teachers', related_query_name='teacher')

class TeacherClass(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, blank=True, null=True)
    class_name = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(default=datetime.datetime.now)