
class Animal:
    edad = None
    nombre = None

    def __init__(self, edad, nombre) -> None:
        self.edad = edad
        self.nombre = nombre

    def __str__(self) -> str:
        return f"edad: {self.edad}\nnombre: {self.nombre}"

    def getEdad(self) -> int:
        return self.edad

    def getNombre(self) -> str:
        return self.nombre