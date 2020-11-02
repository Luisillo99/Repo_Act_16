# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import json
from .particula import Particula
class Organizador:
    def __init__(self):
        self.org = []

    def __str__(self):
        return ''.join(
            str(i) + '\n' for i in self.org
        )

    def agregar_inicio(self,part):
        self.org.insert(0,part)

    def agregar_final(self,part):
        self.org.append(part)

    def mostrar(self):
        for i in self.org:
            print(i)

    def guardar(self,ubicacion):
        try:
            with open(ubicacion,'w') as archivo:
                lista_dict = [i.to_dict() for i in self.org]
                json.dump(lista_dict,archivo, indent=5)
            return 1
        except:
            return 0
    
    def abrir(self,ubicacion):
        try:
            with open(ubicacion,'r') as archivo:
                lista_part = json.load(archivo)
                print(lista_part)
                self.org = [Particula(**i) for i in lista_part]
            return 1
        except:
            return 0