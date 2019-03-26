from rest_framework import routers

from course import views

app_name = 'course'

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet, base_name='course-read-all')
router.register('category', views.CategoryViewSet, base_name='category-read-all')
router.register('chapters', views.ChapterViewSet, base_name='chapters-read-all')
router.register('narrators', views.NarratorViewSet, base_name='narrators-read-all')

urlpatterns = []

urlpatterns += router.urls
