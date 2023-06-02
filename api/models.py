from django.db import models
from django.core.validators import MinValueValidator


class Resume(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='every_resume')
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    title = models.CharField(max_length=256)
    portfolio = models.TextField()
    experience = models.IntegerField(validators=[MinValueValidator(0)])
    education = models.CharField(max_length=256)
    salary = models.IntegerField(validators=[MinValueValidator(0)])
    specialty = models.CharField(max_length=256)
    grade = models.CharField(max_length=25)
    status = models.CharField(max_length=25)

    class Meta:
        ordering = ['title']
