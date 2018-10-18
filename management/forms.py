from django import forms
from .models import StudentClass, Subject



class ClassForm(forms.ModelForm):
    class Meta:
        model = StudentClass
        fields = "__all__"


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'