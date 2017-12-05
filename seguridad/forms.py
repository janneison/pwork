from django import forms
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm
)
from seguridad.models import (User, Trabajo)
# Register your models here.

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

class PostForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ('fecha', 'nombre','descripcion',)
        widgets = {'fecha': forms.DateInput(attrs={'class':'datepicker'}),}