from rest_framework import serializers
from .models import Author, Book
import datetime

# BookSerializer serialize all Book fields and include validation for publication_year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")

# AuthorSerializer serialize the name field and nests BookSerializer for related books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']