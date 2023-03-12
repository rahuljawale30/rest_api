from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response  # to response the get method
from rest_framework import status
from django.http import Http404
from .models import Course, CourseSerializer
# Create your views here.
# it is a sub class of APIView for that import from rest frame work
class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()  # retrive the all field in db
        courseSerializer = CourseSerializer(courses, many=True)  # serializer the retrive data which take from db
        return Response(courseSerializer.data)

    def post(self, request):
        courseSerializer = CourseSerializer(data= request.data)
        if courseSerializer.is_valid():
            courseSerializer.save() # if data valid the save in db and return response
            return Response(courseSerializer.data, status=status.HTTP_201_CREATED)
        return Response(courseSerializer.errors)  # if data is invalid then retun the errors

class CourseDetailView(APIView):

    def get_course(self, pk):
        try:
            return Course.objects.get(pk = pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        course = self.get_course(pk) # this is the data in database get id now serilizers it
        serilizer = CourseSerializer(course)
        return Response(serilizer.data)

    def delete(self, request, pk):
        self.get_course(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk):
        course = self.get_course(pk)
        courseSerializer = CourseSerializer(course, data=request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data)
        return Response(courseSerializer.errors)