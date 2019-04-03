from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from podcast import models, serializers


class SeasonViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [AllowAny, ]
	queryset = models.Season.objects.all()
	search_fields = ('name',)

	def get_serializer_class(self):
		if self.action == 'retrieve':
			return serializers.SeasonRetrieveSerializer
		return serializers.SeasonSerializer
