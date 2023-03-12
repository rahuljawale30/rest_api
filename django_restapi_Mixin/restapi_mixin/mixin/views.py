from django.shortcuts import render
from rest_framework import mixins, generics
from .models import Course, CourseSerializer

# Create your views here.
# for non primary key
class CourseListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)  # because we use the list model mixin

    def post(self, request): # because we use the mixin create method
        return self.create(request)

# pk based operation
class CourseDetailView( generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
