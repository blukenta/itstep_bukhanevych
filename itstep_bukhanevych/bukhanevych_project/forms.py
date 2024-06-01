from django import forms
from django_recaptcha.fields import ReCaptchaField
from .models import TodoItem

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()

class TodoForm(forms.ModelForm):
    date = forms.DateField(widget = forms.DateInput(attrs={"type":"date"}))
    class Meta:
        model = TodoItem
        fields = ["title", "date"]