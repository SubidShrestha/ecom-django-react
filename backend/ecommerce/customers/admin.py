from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Customer
        fields = ('email','city','location')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Customer
        fields = ('email','city','location')

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Customer
    list_display = ('email','first_name','last_name','is_staff', 'is_active',)
    list_filter = ('email','first_name','last_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password','first_name','last_name','phone','gender','city','location')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name','last_name', 'phone','gender','city','password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email','first_name','last_name','gender')
    ordering = ('email','first_name','last_name')

admin.site.register(Customer,CustomUserAdmin)
