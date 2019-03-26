from django.db import models

from utility.models import File


class Playlist(models.Model):
	name = models.CharField(max_length=256)
	artwork = models.ForeignKey(File, on_delete=models.PROTECT)


class Artist(models.Model):
	name = models.CharField(max_length=256)
	description = models.TextField(null=True, blank=True)
	artwork = models.ForeignKey(File, on_delete=models.PROTECT)


class Album(models.Model):
	name = models.CharField(max_length=256)
	artwork = models.ForeignKey(File, on_delete=models.PROTECT)
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')


class Music(models.Model):
	name = models.CharField(max_length=256)
	file = models.ForeignKey(File, on_delete=models.PROTECT, related_name='musics', verbose_name='Music file')
	artwork = models.ForeignKey(File, on_delete=models.PROTECT, related_name='music_artwork')
	playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='musics')
	album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musics')
