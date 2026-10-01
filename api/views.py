from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from .models import Student, Course, Genre, Book
from .serializers import StudentSerializer, GenreSerializer, BookSerializer


class StudentAPIView(APIView):
    def get(self, request: Request, pk: int = None):
        if pk is None:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
        else:
            student = get_object_or_404(Student, pk=pk)
            return Response(StudentSerializer(student).data)

    def post(self, request, pk: int= None):
        if pk:
            return Response({"message": "Method POST not allowed"}, status = status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = StudentSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)

    def put(self, request, pk: int = None):
        if not pk:
            return Response({"message": "Method PUT not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(data=request.data, instance=student)
        serializer.is_valid(raise_exception=True)
        return Response(StudentSerializer(serializer.save()).data)

    def delete(self, request, pk: int = None ):
        if not pk:
            return Response({"message": "Method DELETE not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        student = get_object_or_404(Student, pk=k)
        student.delete()
        return Response({"message": "Student deleted successful"}, status=status.HTTP_204_NO_CONTENT)



class GenreAPIView(APIView):
    def get(self, request: Request, pk: int = None):
        if pk is None:
            genres = Genre.objects.all()
            serializer = GenreSerializer(genres, many=True)
            return Response(serializer.data)
        else:
            genre = get_object_or_404(Genre, pk=pk)
            return Response(GenreSerializer(genre).data)

    def post(self, request, pk: int = None):
        if pk:
            return Response({"message": "Method POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        genre = serializer.save()
        return Response(GenreSerializer(genre).data, status=status.HTTP_201_CREATED)

    def put(self, request, pk: int = None):
        if not pk:
            return Response({"message": "Method PUT not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        genre = get_object_or_404(Genre, pk=pk)
        serializer = GenreSerializer(data=request.data, instance=genre)
        serializer.is_valid(raise_exception=True)
        return Response(GenreSerializer(serializer.save()).data)

    def delete(self, request, pk: int = None):
        if not pk:
            return Response({"message": "Method DELETE not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        genre = get_object_or_404(Genre, pk=pk)
        genre.delete()
        return Response({"message": "Genre deleted successful"}, status=status.HTTP_204_NO_CONTENT)


class BookAPIView(APIView):
    def get(self, request: Request, pk: int = None):
        if pk is None:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            book = get_object_or_404(Book, pk=pk)
            return Response(BookSerializer(book).data)

    def post(self, request, pk: int = None):
        if pk:
            return Response({"message": "Method POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.save()
        return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)

    def put(self, request, pk: int = None):
        if not pk:
            return Response({"message": "Method PUT not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(data=request.data, instance=book)
        serializer.is_valid(raise_exception=True)
        return Response(BookSerializer(serializer.save()).data)

    def delete(self, request, pk: int = None):
        if not pk:
            return Response({"message": "Method DELETE not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response({"message": "Book deleted successful"}, status=status.HTTP_204_NO_CONTENT)
