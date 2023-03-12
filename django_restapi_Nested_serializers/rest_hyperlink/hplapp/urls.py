from django.contrib import admin
from django.urls import path
from .views import CourseListView, InstructorListView, CourseDetailView, InstructorDetailView

urlpatterns = [
    path('instructors/', InstructorListView.as_view()),
    path('course/', CourseListView.as_view()),
    path('course/<int:pk>',CourseDetailView.as_view(), name='course-detail'),
    path('instructors/<int:pk>', InstructorDetailView.as_view(), name='instructor-detail')
]