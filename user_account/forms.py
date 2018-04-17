from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import UserAccount
DOC_TYPE = (
    ('Passaporte', 'Passaporte'),
    ('Carta de Conducao', 'Carta de Conducao'),
    ('BI', 'BI'),
    ('DIRE', 'DIRE'),
)
GENDER = (
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'long'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'long'}))
    gender = forms.CharField(widget=forms.Select(attrs={'class': 'long'},choices=GENDER))
    doc_type = forms.CharField(widget=forms.Select(attrs={'class': 'long'},choices=DOC_TYPE))
    doc_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'long'}))
    contact1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'long'}), required=False)
    contact2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'long'}), required=False)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'long'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}),
                                    required=False)
    enrollment_year = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}),
                                      required=False)

    class Meta:
        model = UserAccount
        fields = ('code','first_name','last_name','gender','doc_type','doc_id'
                  , 'contact1','contact2','address','date_of_birth','enrollment_year')

    def clean_code(self):
        code = self.cleaned_data.get('code')
        qs = UserAccount.objects.filter(code=code)
        if qs.exists():
            raise forms.ValidationError("este codigo de estudante ja existe")
        return code

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Combinacao incorecta de password")
        return password2



class UserAccountAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = UserAccount
        fields = ('code',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Combinacao incorrecta de password")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAccountAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAccountAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserAccount
        fields = ('code', 'password', 'active', 'admin','is_student','is_teacher')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]