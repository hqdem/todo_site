from django import forms
from allauth.account.forms import LoginForm, SignupForm

from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Добавить новую задачу...'}), label='Наименование')
    is_completed = forms.BooleanField(label='Завершено', required=False)

    class Meta:
        model = Task
        fields = ['title', 'is_completed']


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
