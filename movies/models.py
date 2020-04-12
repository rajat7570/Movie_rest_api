from django.db import models

# Create your models here.
# posts/models.py


class Movie(models.Model):
    title = models.CharField(max_length=100)
    ratings = models.IntegerField()
    release_date = models.DateField()
    summary = models.TextField()

    @property
    def __str__(self):
        return self.title

