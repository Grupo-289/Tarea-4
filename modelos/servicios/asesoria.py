from modelos.servicio import Servicio

class Asesoria(Servicio):

    def calcular_costo(self, horas):
        return self.tarifa * horas

    def descripcion(self):
        return "Servicio de asesoría especializada"
    