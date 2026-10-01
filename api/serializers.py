from typing import Any

from rest_framework import serializers

from .models import Student, Genre, Book


class StudentSerializer(serializers.Serializer):
    id = serializers.BigIntegerField(read_only=True)
    full_name = serializers.CharField(max_length=255, required=True)
    phone_number = serializers.CharField(max_length=13, default="+998991234567")
    birth_year = serializers.IntegerField(default=2010)
    image = serializers.ImageField(required=False)
    address = serializers.CharField(max_length=255, required=False)
    course_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance: Student, validated_data ):
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.birth_year = validated_data.get("birth_year", instance.birth_year)
        instance.address = validated_data.get("address", instance.address)
        instance.course_id = validated_data.get("course_id", instance.course_id)
        instance.save()
        return instance


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, required=True)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance: Genre, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255, required=True)
    author = serializers.CharField(max_length=255, required=True)
    pages = serializers.IntegerField(default=100)
    published_year = serializers.IntegerField(default=2020)
    genre_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance: Book, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.pages = validated_data.get("pages", instance.pages)
        instance.published_year = validated_data.get("published_year", instance.published_year)
        instance.genre_id = validated_data.get("genre_id", instance.genre_id)
        instance.save()
        return instance
