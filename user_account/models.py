from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

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
class UserAccountManager(BaseUserManager):
    def create_user(self, code, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not code:
            raise ValueError('o estudante deve ter codigo de estudante')

        user = self.model(
            code = code,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, code, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            code,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, code, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            code,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class UserAccount(AbstractBaseUser):
    code = models.CharField(verbose_name='code',unique=True,max_length=155)
    first_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    gender = models.CharField(max_length=200,blank=True, choices=GENDER)
    email = models.EmailField(blank=True)
    date_of_birth = models.DateField(blank=True,null=True)
    doc_type = models.CharField(max_length=255, choices=DOC_TYPE,blank=True)
    doc_id = models.CharField(max_length=155,blank=True)
    contact1 = models.IntegerField(blank=True,null=True)
    contact2 = models.IntegerField(blank=True,null=True)
    enrollment_year = models.DateField(blank=True,null=True)
    address = models.CharField(max_length=150,blank=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that's built in.
    objects = UserAccountManager()

    USERNAME_FIELD = 'code'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.code

    def get_short_name(self):
        # The user is identified by their email address
        return self.code

    def __str__(self):              # __unicode__ on Python 2
        return self.code

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active