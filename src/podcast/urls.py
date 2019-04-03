from rest_framework import routers

from podcast import views

app_name = 'podcast'

router = routers.DefaultRouter()
router.register('podcasts', views.SeasonViewSet, base_name='podcast-read-all')

urlpatterns = []

urlpatterns += router.urls
