from modelos.entidad import Entidad

class Cliente(Entidad):

    def __init__(self, nombre, correo):
        self.__nombre = nombre
        self.__correo = correo

        if "@" not in correo:
            raise ValueError("Correo inválido")

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - {self.__correo}"