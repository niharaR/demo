from  django import forms
from django.db import models
from .models import movie
from django.forms import ModelForm


class MovieForm(forms.ModelForm):
    class Meta:
        model=movie
        fields=['name','desc','year','img']