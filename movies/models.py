from django.db import models

# Create your models here.
class Movie (models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.CharField(max_length=30, null=False)
    genre = {
        ('A', 'Acción'),
        ('T', 'Terror'),
        ('D', 'Drama'),
        ('C', 'Comedia'),
    }
    movie_genre = models.CharField(max_length=10, choices=genre, null=False)
    name_director = models.CharField(max_length=30, null=False)
    year= models.DateField(auto_now=False, null=False)
    sinopsis = models.TextField(null=False)

    def __str__(self):
        return self.movie