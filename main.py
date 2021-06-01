from claseBus import Bus
from cliente import Cliente
from gestorBuses import GestorBuses




gestor = GestorBuses()

opcion = input(int("Escoge una opción: 1. Añadir autobús 2. Eliminar autobús"))


bus = Bus(5, 2)
cliente1 = Cliente("Joan")
cliente2 = Cliente("Gabri")

bus.venta(cliente1)
bus.venta(cliente2)
bus.retorno(cliente1)
gestor.anadirBus(bus)
print(gestor)

