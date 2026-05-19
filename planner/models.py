from django.db import models

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    exam_date = models.DateField()
    study_date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject_name