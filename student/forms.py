from django.db import transaction
from django.forms import ModelForm, Textarea
from django import forms

from user_account.forms import RegisterForm
from user_account.models import UserAccount
from student.models import Student


class StudentForm(RegisterForm):
    quotes = forms.CharField(widget=forms.TextInput(attrs={'class': 'long'}), required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': '', 'rows': '2'}), required=False)
    profile_photo = forms.FileField(widget=forms.FileInput(attrs={'class': ''}), required=False)
    course = forms.CharField(widget=forms.TextInput(attrs={'class': 'long'}), required=False)

    class Meta(RegisterForm.Meta):
        model = UserAccount

    @transaction.atomic
    def save(self,commit=False):
        account = super().save(commit=False)
        account.is_student = True
        account.save()
        student = Student.objects.create(student_account=account)
        student.quotes = self.cleaned_data.get('quotes')
        student.bio = self.cleaned_data.get('bio')
        student.profile_photo = self.cleaned_data.get('profile_photo')
        student.save()
        return account