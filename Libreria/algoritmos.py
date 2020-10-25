# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    dist = math.sqrt((x_1-x_2)**2+(y_1-y_2)**2)
    return dist
    