from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100, null=False)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    review = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])