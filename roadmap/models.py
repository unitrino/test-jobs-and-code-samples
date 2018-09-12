from django.db import models
from django.contrib.auth.models import User


class Step(models.Model):
    name = models.CharField(max_length=100)
    explanation = models.TextField()

    def __str__(self):
        return self.name


class Roadmap(models.Model):
    name = models.CharField(max_length=100)
    steps = models.ManyToManyField(Step)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
