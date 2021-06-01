from claseBus import Bus
from cliente import Cliente

bus = Bus(5)
cliente1 = Cliente("Joan")
cliente2 = Cliente("Gabri")
print(bus)
bus.venta(cliente1)
print(bus)
bus.venta(cliente2)
print(bus)
bus.retorno(cliente1)
print(bus)

