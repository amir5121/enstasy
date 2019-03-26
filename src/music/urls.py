from rest_framework import routers

from music import views

app_name = 'music'

router = routers.DefaultRouter()
router.register('musics', views.MusicViewSet, base_name='music-read-all')
router.register('playlist', views.PlaylistViewSet, base_name='playlist-read-all')
router.register('albums', views.AlbumViewSet, base_name='album-read-all')
router.register('artists', views.ArtistViewSet, base_name='artists-read-all')

urlpatterns = []

urlpatterns += router.urls
