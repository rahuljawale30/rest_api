
import re
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework import authentication
from .serializers import InstructorSerializer, CourseSerializer
from .models import Instructor, Course
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.authentication import BasicAuthentication


# users = User.objects.all()
# for user in users:
#     token = Token.objects.get_or_create(user=user)
#     print(token)


class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        print('insidnde has permission', request.user)
        user = request.user
        if request.method == 'GET':
            return True

        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_superuser:
                return True

        return False


class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()


class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()


class CourseListView(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]  # here we add the session authentication
    permission_classes = [IsAuthenticated,WriteByAdminOnlyPermission]  # here we add the session authentication
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


# line 45--session authentication mein broswers se login karne ke baad access kr skte hai username or password send karte hai or session help se authentication check krte hai
# line 44 -- Basic authentication mein hum username or passward send krte hai by url

# when we add the course then we user login nhi hai Admin ho to add kar skata hai -- for that import IsAdminUser
# create own class means admin add kr skata hai but see anyone  import basePermission