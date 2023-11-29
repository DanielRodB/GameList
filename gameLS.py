#Libreria de juegos
from datetime import datetime
storage = list()


class LibraryBase():
    gameTittle = ""
    gameClass = ""
    gameOnline = ""
    gameRelease = ""
    gamePrice = ""
    def library(self,):
        self.gameTittle = str(input(('Escriba el título del juego: ')))
        storage.append(self.gameTittle)
        self.gameRelease = datetime(input(('Escriba la fecha de estreno: ')))
        storage.append(self.gameRelease)
        self.gamePrice = float(input(('Escriba el precio del juego: ')))
        storage.append(self.gamePrice)
        self.gameClass = str(input(('Escriba la clasificación del juego: ')))
        storage.append(self.gameClass)
        self.gameOnline = bool(input(('¿Se puede jugar online? ')))
        storage.append(self.gameOnline)




def show_libraries():
    print("El nombre del juego es: " + storage["Nombre"])
    print("EL ID del juego es: " + storage["id"])

gate = ""
LibraryBase.library(gate)

print(str(gate))
