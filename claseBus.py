class Bus:
	def __init__(self, plazas):
		self.__plazas = plazas
		self.__plazasOcupadas = 0

	

	def retorno(self, billetesADevolver):
    	if(billetesADevolver < self.__plazasOcupadas):
    		return self.getPlazasLibres()
		else:
    		self.__plazasOcupadas -= billetesADevolver
			return self.getPlazasLibres()
