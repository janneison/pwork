from django.contrib import admin

from seguridad.models import (User, Trabajo)
# Register your models here.

from django.contrib.auth.admin import UserAdmin
from seguridad.forms import (
    CustomUserChangeForm,
    CustomUserCreationForm
)

class AdminTrabajo(admin.ModelAdmin):
	list_display=('nombre','descripcion')
	search_fields=('nombre','descripcion')		

admin.site.register(Trabajo,AdminTrabajo)

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (
            None, {
                'fields': (
                    'cargo',
                )
            }
        ),
    )

class UserAdmin(CustomUserAdmin):
    list_display =  (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'is_superuser',
        'cargo',
        'last_login',
        'date_joined'
    )


admin.site.register(User,UserAdmin)