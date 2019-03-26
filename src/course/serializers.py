from rest_framework import serializers

from course import models
from utility.models import File


class NarratorSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')

	class Meta:
		model = models.Narrator
		fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	narrator = NarratorSerializer()

	class Meta:
		model = models.Chapter
		fields = '__all__'


class ChapterForNarratorSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')

	class Meta:
		model = models.Chapter
		exclude = ['narrator', ]


class CategorySerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')

	class Meta:
		model = models.Category
		fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	files = serializers.SlugRelatedField(many=True, read_only=True, slug_field='address')
	chapter = ChapterSerializer()
	category = CategorySerializer()

	class Meta:
		model = models.Course
		fields = '__all__'


class CourseForChapterSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	file = serializers.CharField(source='file.address')

	class Meta:
		model = models.Course
		exclude = ['chapter', 'category']


class CourseForCategorySerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	file = serializers.CharField(source='file.address')
	chapter = ChapterSerializer()

	class Meta:
		model = models.Course
		fields = '__all__'


class CategoryRetrieveSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	courses = CourseForCategorySerializer(many=True)

	class Meta:
		model = models.Category
		fields = '__all__'


class ChapterRetrieveSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	narrator = NarratorSerializer()
	courses = CourseForChapterSerializer(many=True)

	class Meta:
		model = models.Chapter
		fields = '__all__'


class NarratorRetrieveSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	chapters = ChapterForNarratorSerializer(many=True)

	class Meta:
		model = models.Narrator
		fields = '__all__'
