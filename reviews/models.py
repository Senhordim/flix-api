from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField(
      validators=[
          MinValueValidator(1, 'Avaliação não pode ser inferior a 0'),
          MaxValueValidator(5, 'Avaliação não pode ser superior a 5')
      ]
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie
