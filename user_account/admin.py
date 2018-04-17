from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAccountAdminCreationForm, UserAccountAdminChangeForm
from .models import UserAccount

class UserAccountAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAccountAdminChangeForm
    add_form = UserAccountAdminCreationForm

    # The fields to be used in displaying the Account model.
    # These override the definitions on the base AccountAdmin
    # that reference specific fields on auth.Account.
    list_display = ('code', 'admin','is_teacher','is_student','first_name','address')
    list_filter = ('admin','is_teacher','is_student')
    fieldsets = (
        (None, {'fields': ('code', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. AccountAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('code', 'password1', 'password2')}
        ),
    )
    search_fields = ('code',)
    ordering = ('code',)
    filter_horizontal = ()


admin.site.register(UserAccount, UserAccountAdmin)



# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)