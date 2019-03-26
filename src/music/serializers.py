from rest_framework import serializers

from music import models


class ArtistSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')

	class Meta:
		model = models.Artist
		fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	artist = ArtistSerializer()

	class Meta:
		model = models.Album
		fields = '__all__'


class AlbumForArtistSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')

	class Meta:
		model = models.Album
		exclude = ['artist', ]


class PlaylistSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')

	class Meta:
		model = models.Playlist
		fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	file = serializers.CharField(source='file.address')
	album = AlbumSerializer()
	playlist = PlaylistSerializer()

	class Meta:
		model = models.Music
		fields = '__all__'


class MusicForAlbumSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	file = serializers.CharField(source='file.address')

	class Meta:
		model = models.Music
		exclude = ['album', 'playlist']


class MusicForPlaylistSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	file = serializers.CharField(source='file.address')
	album = AlbumSerializer()

	class Meta:
		model = models.Music
		fields = '__all__'


class PlaylistRetrieveSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	musics = MusicForPlaylistSerializer(many=True)

	class Meta:
		model = models.Playlist
		fields = '__all__'


class AlbumRetrieveSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	artist = ArtistSerializer()
	musics = MusicForAlbumSerializer(many=True)

	class Meta:
		model = models.Album
		fields = '__all__'


class ArtistRetrieveSerializer(serializers.ModelSerializer):
	artwork = serializers.CharField(source='artwork.address')
	albums = AlbumForArtistSerializer(many=True)

	class Meta:
		model = models.Artist
		fields = '__all__'
