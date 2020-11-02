# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from .algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, Id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue):
        self.__id = Id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(origen_x,origen_y,destino_x,destino_y)

    def __str__(self):
        return (
            'ID: '+str(self.__id)+'\n'
            'Origen en x: '+str(self.__origen_x)+'\n'
            'Origen en y: '+str(self.__origen_y)+'\n'
            'Destino en x: '+str(self.__destino_x)+'\n'
            'Destino en y: '+str(self.__destino_y)+'\n'
            'velocidad: '+str(self.__velocidad)+'\n'
            'Red: '+str(self.__red)+'\n'
            'Green: '+str(self.__green)+'\n'
            'Blue: '+str(self.__blue)+'\n'
            'Distancia: '+str(self.__distancia)+'\n'
        )

    def to_dict(self):
        return ( 
            {
                'Id':self.__id,
                'origen_x':self.__origen_x,
                'origen_y':self.__origen_y,
                'destino_x':self.__destino_x,
                'destino_y':self.__destino_y,
                'velocidad':self.__velocidad,
                'red':self.__red,
                'green':self.__green,
                'blue':self.__blue,
            }
        )