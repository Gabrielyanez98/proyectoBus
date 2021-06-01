import billete

class Bus:
	def __init__(self, plazas):
		self.__plazas = plazas
		self.__billetes = []


	def getPlazasLibres(self):
		return self.__plazas - len(self.__billetes)

	def retorno(self):
		if(len(self.__billetes) > len(self.__billetes)):
			return self.getPlazasLibres()
		else:
			return self.getPlazasLibres()
	
	def venta(self, cliente):
	
		if len(self.__billetes) > self.getPlazasLibres():
    			return self.getPlazasLibres()
		else:
			billete=Billete(cliente)
			self.__billetes.append(billete)
			return self.getPlazasLibres()

	def __str__(self):
		return "\n\tPlazas: "+ str(self.__plazas) + "\n\tPlazas libres: "+ str(self.getPlazasLibres())

