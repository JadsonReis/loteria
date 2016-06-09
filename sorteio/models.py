from django.db import models
from datetime import datetime

class Concursos(models.Model):
	concurso = models.IntegerField(primary_key=True)
	data = models.DateField(default=datetime.now())
	dezena1 = models.CharField(max_length=2)
	dezena2 = models.CharField(max_length=2)
	dezena3 = models.CharField(max_length=2)
	dezena4 = models.CharField(max_length=2)
	dezena5 = models.CharField(max_length=2)
	dezena6 = models.CharField(max_length=2)
	arr_total = models.CharField(max_length=255, null=True)
	gan_sena = models.CharField(max_length=255, null=True)
	cidade = models.CharField(max_length=255, null=True)
	uf = models.CharField(max_length=2, null=True)
	rat_sena = models.CharField(max_length=255, null=True)
	gan_quina = models.CharField(max_length=255, null=True)
	rat_quina = models.CharField(max_length=255, null=True)
	gan_quadra = models.CharField(max_length=255, null=True)
	rat_quadra = models.CharField(max_length=255, null=True)
	acumulado = models.CharField(max_length=255, null=True)
	val_acumulado = models.CharField(max_length=255, null=True)
	est_premio = models.CharField(max_length=255, null=True)
	acumulado_mega_virada = models.CharField(max_length=255, null=True)

	def __str__(self):
		return '%s' % self.concurso

	def sort_data(self):
		import operator

		data = {}
		for concurso in Concursos.objects.values_list:
			for i in range(2,8):
				if concurso[i] in data:
					data['value']++
				else:
					data = {'data': concurso[i], 'value': 1}

		return sorted_d = sorted(data.items(), key=operator.itemgetter(1))
					

	def max_sort(self):
		self.sort_data()
		pass

	def min_sort(self):
		pass

