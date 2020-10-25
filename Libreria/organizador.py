# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

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
