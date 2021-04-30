from django import forms
from .models import Student

class PostForm(forms.ModelForm):
    class Meta(object):
        model = Student
        fields = '__all__'