from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Discipline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Athlete(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    disciplines = models.ManyToManyField(Discipline)

    def __str__(self):
        return self.name