from django.shortcuts import render
from rest_framework import generics
from .serializers import InstructorSerializer, CourseSerilizer
from .models import Instructor, Course
# Create your views here.
class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

class CourseListView(generics.ListCreateAPIView):
    serializer_class = CourseSerilizer
    queryset = Course.objects.all()

