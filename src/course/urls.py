from rest_framework import routers

from music import views

app_name = 'course'

router = routers.DefaultRouter()
router.register('courses', views.MusicViewSet, base_name='course-read-all')
router.register('category', views.PlaylistViewSet, base_name='category-read-all')
router.register('chapters', views.AlbumViewSet, base_name='chapters-read-all')
router.register('narrators', views.ArtistViewSet, base_name='narrators-read-all')

urlpatterns = []

urlpatterns += router.urls
