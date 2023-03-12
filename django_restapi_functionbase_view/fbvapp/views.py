from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer


# Create your views here.
# non primary key operation

@api_view(['GET','POST'])
def courseListView(request):
    # check the request is get or post
    if request.method == 'GET':
        courses = Course.objects.all()  # retrive the all field in db
        courseSerializer = CourseSerializer(courses, many=True) #serializer the retrive data which take from db
        return Response(courseSerializer.data)

    elif request.method == 'POST':
        # check the request data is valid or not in db for that post method call the valid method so write the valid method in seializer file
        courseSerializer = CourseSerializer(data= request.data)
        if courseSerializer.is_valid():
            courseSerializer.save() # if data valid the save in db and return response
            return Response(courseSerializer.data, status=status.HTTP_201_CREATED)
        return Response(courseSerializer.errors)  # if data is invalid then retun the errors


# primaary key based operation
@api_view(['GET','PUT','DELETE'])
def courseDetailView(request, pk):
    # first access the pk object for that use try and except for handle the error because get show the doesnotexist error
    try:
        course = Course.objects.get(pk=pk) # means get id == primary key provode by user
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) # if pk in not in db then return error status import from rest framework that show all error

    if request.method == 'GET':
        courseSerializer = CourseSerializer(course)
        return Response(courseSerializer.data)

    elif request.method == 'PUT':
        courseSerializer = CourseSerializer(course, data=request.data)  # mean the data in put request is serializer then
        if courseSerializer.is_valid():  # if data is valid then save
            courseSerializer.save()
            return Response(courseSerializer.data)
        return Response(courseSerializer.errors)

    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)