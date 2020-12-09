# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import json
from .particula import Particula
from pprint import pformat
class Organizador:
    def __init__(self):
        self.__org = []
        self.grafo_dic = dict()

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

    def orden(self, as_des, atributo):
        if atributo == "id":
            self.__org.sort(key=lambda particula: particula.id, reverse=as_des)
        if atributo == "dis":
            self.__org.sort(key=lambda particula: particula.dis, reverse=as_des)
        if atributo == "vel":
            self.__org.sort(key=lambda particula: particula.vel, reverse=as_des)

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

    def grafo(self):
        for part in self.__org:
            origen = (part.or_x, part.or_y)
            destino = (part.de_x, part.de_y)
            if origen in self.grafo_dic:
                if (destino,round(part.dis,2)) in self.grafo_dic[origen]:
                    pass
                else:
                    self.grafo_dic[origen].append((destino,round(part.dis,2)))
            else:
                self.grafo_dic[origen] = [(destino,round(part.dis,2))]
            
            if destino in self.grafo_dic:
                if (origen,round(part.dis,2)) in self.grafo_dic[destino]:
                    pass
                else:
                    self.grafo_dic[destino].append((origen,round(part.dis,2)))
            else:
                self.grafo_dic[destino] = [(origen,round(part.dis,2))]
        string = pformat(self.grafo_dic, width=40) 
        return(string)
    
    def borrar_grafo(self):
        self.grafo_dic.clear()

    def profundidad(self, ini_x, ini_y):
        try:
            vertice = (ini_x,ini_y)
            visitados = []
            pila = []
            recorrido = []
            visitados.append(vertice)
            pila.append(vertice)
            while len(pila) > 0:
                vertice = pila[(len(pila)-1)]
                recorrido.append(vertice)
                pila.pop()
                for ady in self.grafo_dic[vertice]:
                    if ady[0] in visitados:
                        pass
                    else:
                        visitados.append(ady[0])
                        pila.append(ady[0])
            string = pformat(recorrido, width=40) 
            return string

        except KeyError:
            return "El vértice inicial no fue encontrado"

    def amplitud(self, ini_x, ini_y):
        try:
            vertice = (ini_x,ini_y)
            visitados = []
            pila = []
            recorrido = []
            visitados.append(vertice)
            pila.append(vertice)

            while len(pila) > 0:
                vertice = pila[(len(pila)-1)]
                recorrido.append(vertice)
                pila.pop()

                for ady in self.grafo_dic[vertice]:
                    if ady[0] in visitados:
                        pass
                    else:
                        visitados.append(ady[0])
                        pila.insert(0, ady[0])
            string = pformat(recorrido, width=40) 
            return string
        except KeyError:
            return "El vertice inicial no fue encontrado"