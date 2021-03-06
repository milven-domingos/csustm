# Generated by Django 2.0 on 2018-04-15 10:28

import csustm.file_validation
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', csustm.file_validation.ContentTypeRestrictedFileField(blank=True, default='none.jpg', upload_to=csustm.file_validation.get_upload_image)),
                ('quotes', models.CharField(blank=True, max_length=155)),
                ('bio', models.TextField(blank=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('course', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('student_account', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='students', related_query_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
                ('student_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.ClassName')),
            ],
        ),
        migrations.CreateModel(
            name='StudentMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.FloatField(blank=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('class_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.ClassName')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Subject')),
            ],
        ),
    ]
