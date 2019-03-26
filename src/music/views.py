from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from music import models, serializers


class MusicViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [AllowAny, ]
	queryset = models.Music.objects.all()
	serializer_class = serializers.MusicSerializer
	search_fields = ('name', 'playlist__name', 'album__name', 'album__artist__name')


class PlaylistViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [AllowAny, ]
	queryset = models.Playlist.objects.all()
	search_fields = ('name',)

	def get_serializer_class(self):
		if self.action == 'retrieve':
			return serializers.PlaylistRetrieveSerializer
		return serializers.PlaylistSerializer


class AlbumViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [AllowAny, ]
	queryset = models.Album.objects.all()
	search_fields = ('name',)

	def get_serializer_class(self):
		if self.action == 'retrieve':
			return serializers.AlbumRetrieveSerializer
		return serializers.AlbumSerializer


class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [AllowAny, ]
	queryset = models.Artist.objects.all()
	search_fields = ('name',)

	def get_serializer_class(self):
		if self.action == 'retrieve':
			return serializers.ArtistRetrieveSerializer
		return serializers.ArtistSerializer
