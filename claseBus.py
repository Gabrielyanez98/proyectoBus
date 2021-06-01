import billete

class Bus:
	def __init__(self, plazas, billetes):
		self.__plazas = plazas
		self.__plazasOcupadas = 0
		self.__billetes = billetes


	def getPlazasLibres(self):
		return self.__plazas - self.__plazasOcupadas

	def retorno(self):
		if(self.__billetes > self.__plazasOcupadas):
			return self.getPlazasLibres()
		else:
			self.__plazasOcupadas -= self.__billetes
			return self.getPlazasLibres()
	
	def venta(self, cliente):
	
		if self.__billetes > self.getPlazasLibres():
    			return self.getPlazasLibres()
		else:
			self.__plazasOcupadas += self.__billetes
			billete=Billete(cliente)
			self.__billetes.append(billete)
			return self.getPlazasLibres()

	def __str__(self):
		return "\n\tPlazas: "+ str(self.__plazas) + "\n\tPlazas libres: "+ str(self.getPlazasLibres())

bus = Bus(5)
bus.venta(3)
print(bus)
bus.retorno()
print(bus)
