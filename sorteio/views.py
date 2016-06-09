from .models import Concursos
from .serializers import ConcursosSerializer
from rest_framework.generics import ListApiView



class DezenasMaisSorteadas(ListApiView):
	queryset = Concursos.objects.all()
	serializer = ConcursosSerializer


class DezenasMenosSorteadas(ListApiView):
	queryset = Concursos,objects.all()
	serializer = ConcursosSerializer

