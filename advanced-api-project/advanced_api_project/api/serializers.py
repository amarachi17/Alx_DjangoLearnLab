from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

        def validate_publication_year(self, value):
            # Checking if publication year is in the future and making sure its not.
            current_year = datetime.datetime.now().year
            if value > current_year:
                raise serializers.ValidationError("Publication year cannot be in the future.")
            raise value
        
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) # Making a nested Serializer 

    class Meta:
        model = Author
        fields = ['name', 'books']