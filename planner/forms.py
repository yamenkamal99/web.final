from django import forms
from .models import Subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name', 'exam_date', 'study_date', 'notes']

        widgets = {
            'exam_date': forms.DateInput(attrs={'type': 'date'}),
            'study_date': forms.DateInput(attrs={'type': 'date'}),
               }