from django.urls import path

from .views import StudentAPIView, GenreAPIView, BookAPIView


urlpatterns = [
    path('students/', StudentAPIView.as_view()),
    path('students/<int:pk>/', StudentAPIView.as_view()),
    path('genres/', GenreAPIView.as_view()),
    path('genres/<int:pk>/', GenreAPIView.as_view()),
    path('books/', BookAPIView.as_view()),
    path('books/<int:pk>/', BookAPIView.as_view()),
]