from .models import Course, Instructor
from rest_framework import serializers

# class CourseSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = '__all__'
#
# class InstructorSerializer(serializers.ModelSerializer):
#     courses = CourseSerilizer(many=True, read_only=True)
#     class Meta:
#         model = Instructor
#         fields = '__all__'

# when we want to the instructor object then
class InstructorSerializer(serializers.ModelSerializer):
    # courses = CourseSerilizer(many=True, read_only=True)
    class Meta:
        model = Instructor
        fields = '__all__'

class CourseSerilizer(serializers.ModelSerializer):
    instructor = InstructorSerializer(read_only= True)
    class Meta:
        model = Course
        fields = '__all__'