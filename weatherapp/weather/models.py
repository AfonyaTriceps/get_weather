from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name
