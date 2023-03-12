from django.shortcuts import render
from .models import Course, CourseSerializer
from rest_framework import mixins, generics

# Create your views here.
#non primary key based operation
# class CourseListView(generics.ListAPIView, generics.CreateAPIView ):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
# primary key based operation
# class CourseDetailView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer


# using combination of Generic view
#non primary key based operation
class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# primary key based operation
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

