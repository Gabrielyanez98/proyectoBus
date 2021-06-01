from billete import Billete

class Bus:
	def __init__(self, plazas, numero):
		self.__plazas = plazas
		self.__billetes = []
		self.__numero = numero

	def getNumero(self):
		return self.__numero

	def getPlazasLibres(self):
		return self.__plazas - len(self.__billetes)

	def retorno(self,cliente):
		if(len(self.__billetes) - 1 < 0):
			return self.getPlazasLibres()
		else:
			for i in range(len(self.__billetes)):
				if self.__billetes[i].getCliente().getNombre() == cliente.getNombre():
					self.__billetes.pop(i)
					return self.getPlazasLibres()
			return self.getPlazasLibres()
	
	def venta(self, cliente):
	
		if 1 > self.getPlazasLibres():
    			return self.getPlazasLibres()
		else:
			billete=Billete(cliente)
			self.__billetes.append(billete)
			return self.getPlazasLibres()

	def __str__(self):
		clientes = ''
		for billete in self.__billetes:
			clientes += '\n\t\t --> ' + billete.getCliente().getNombre()
		return "\n\tPlazas: "+ str(self.__plazas) + "\n\tPlazas libres: "+ str(self.getPlazasLibres()) + "\n\tClientes: "+ clientes

