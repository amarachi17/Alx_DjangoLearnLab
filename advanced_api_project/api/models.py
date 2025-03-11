from django.db import models

# Create your models here.

# Class Author represents a books author   
class Author(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

# Class Book has a title,publication year and a foreign key refrencing Author
class Book(models.Model):
    title = models.CharField(max_length=300)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title