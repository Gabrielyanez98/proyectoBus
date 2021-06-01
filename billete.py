from cliente import Cliente
class Billete:
	def __init__(self, cliente):
		if type(cliente) is Cliente:
			self.__cliente = cliente
		else:
			self.__cliente = Cliente(cliente)

	def getCliente(self):
		return self.__cliente

	def setCliente(self, cliente):
		if type(cliente) is Cliente:
			self.__cliente = cliente
		else:
			self.__cliente = Cliente(cliente)
	