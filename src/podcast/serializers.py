from rest_framework import serializers

from podcast import models


class SeasonSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')

	class Meta:
		model = models.Season
		fields = '__all__'


class PodcastSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	file = serializers.CharField(source='file.address')

	class Meta:
		model = models.Podcast
		exclude = ['chapter']


class SeasonRetrieveSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	podcasts = PodcastSerializer(many=True)

	class Meta:
		model = models.Season
		fields = '__all__'
