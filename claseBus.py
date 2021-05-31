class Bus:
	def __init__(self, plazas):
		self.__plazas = plazas
		self.__plazasOcupadas = 0

	def getPlazasLibres(self):
		return self.__plazas - self.__plazasOcupadas

	# return plazasLibres
	def venta(self, billetesVender):

		if billetesVender > self.getPlazasLibres():
			return self.getPlazasLibres()
		else:
			self.__plazasOcupadas += billetesVender
			return self.getPlazasLibres()

	def __str__(self):
		return "\n\tPlazas: "+ str(self.__plazas) + "\n\tPlazas libres: "+ str(self.getPlazasLibres())
bus = Bus(5)
bus.venta(3)
print(bus)