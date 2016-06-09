from rest_framework.serializers import ModelSerializer

from .models import Concursos

class ConcursosSerializer(ModelSerializer):
	class Meta:
		models = Concursos