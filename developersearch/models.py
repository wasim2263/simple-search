from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Developers(models.Model):
    email = models.EmailField(max_length=254, unique=True, null=False)


class ProgrammingLanguages(models.Model):
    developer = models.ManyToManyField(Developers)
    name = models.CharField(max_length=254, unique=True, null=False)

class Languages(models.Model):
    developer = models.ManyToManyField(Developers)
    code = models.CharField(max_length=254, unique=True, null=False)

class Interviews(models.Model):
    developer = models.ForeignKey(Developers, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(validators=[MinValueValidator(1), MinValueValidator(5)])
    comment = models.TextField(max_length=500)



