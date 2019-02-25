from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=100)
    plot = models.TextField(max_length=500)
    year = models.IntegerField()
    director = models.CharField(max_length=100)

    def __str__(self):
        return self.name