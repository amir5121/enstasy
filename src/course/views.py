from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from course import models, serializers


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [AllowAny, ]
	queryset = models.Course.objects.all()
	serializer_class = serializers.CourseSerializer
	search_fields = ('name', 'category__name', 'chapter__name', 'chapter__narrator__name')


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [AllowAny, ]
	queryset = models.Category.objects.all()
	search_fields = ('name',)

	def get_serializer_class(self):
		if self.action == 'retrieve':
			return serializers.CategoryRetrieveSerializer
		return serializers.CategorySerializer


class ChapterViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [AllowAny, ]
	queryset = models.Chapter.objects.all()
	search_fields = ('name',)

	def get_serializer_class(self):
		if self.action == 'retrieve':
			return serializers.ChapterRetrieveSerializer
		return serializers.ChapterSerializer


class NarratorViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [AllowAny, ]
	queryset = models.Narrator.objects.all()
	search_fields = ('name',)

	def get_serializer_class(self):
		if self.action == 'retrieve':
			return serializers.NarratorRetrieveSerializer
		return serializers.NarratorSerializer
