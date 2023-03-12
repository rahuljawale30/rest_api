from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Course,CourseSerializer
from rest_framework.viewsets import ViewSet

# Create your views here.
# in the view set we create a one class write the method for non primary and primary operation
class CourseViewSet(ViewSet):
    def list(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

    def retrieve(self, request,pk):
        try:
            courses = Course.objects.get(pk=pk)
        except Course.DoestNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(courses)
        return Response(serializer.data)
