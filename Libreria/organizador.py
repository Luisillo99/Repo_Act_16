# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import json
from .particula import Particula
class Organizador:
    def __init__(self):
        self.__org = []

    def __str__(self):
        return ''.join(
            str(i) + '\n' for i in self.__org
        )
    
    def __len__(self):
        return (len(self.__org))

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__org):
            part = self.__org[self.cont]
            self.cont += 1
            return part
        else:
            raise StopIteration

    def agregar_inicio(self,part):
        self.__org.insert(0,part)

    def agregar_final(self,part):
        self.__org.append(part)

    def mostrar(self):
        for i in self.__org:
            print(i)

    def guardar(self,ubicacion):
        try:
            with open(ubicacion,'w') as archivo:
                lista_dict = [i.to_dict() for i in self.__org]
                json.dump(lista_dict,archivo, indent=5)
            return 1
        except:
            return 0
    
    def abrir(self,ubicacion):
        try:
            with open(ubicacion,'r') as archivo:
                lista_part = json.load(archivo)
                print(lista_part)
                self.__org = [Particula(**i) for i in lista_part]
            return 1
        except:
            return 0