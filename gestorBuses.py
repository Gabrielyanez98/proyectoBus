class GestorBuses():
    def __init__(self):
        self.__autobuses = []

    def anadirBus(self, autobus):
        self.__autobuses.append(autobus)

    def eliminarBus(self, autobus):
        for i in range(len(self.__autobuses)):
            if self.__autobuses[i].getNumero() == autobus:
                self.__autobuses.pop(i)
    def __str__(self):
        buses = ''
        for autobus in self.__autobuses:
            
            buses += str(autobus)
        return buses