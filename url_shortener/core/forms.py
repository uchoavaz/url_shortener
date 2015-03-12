from django import forms
from django.conf import settings
from django.forms import ModelForm
from .models import Url


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['original_url', 'short_url','is_protected','url_password','email','slug']