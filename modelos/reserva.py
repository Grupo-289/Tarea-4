class Reserva:
    
    def __init__(self, cliente, servicio, horas):
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar(self):
        if self.horas <= 0:
            raise ValueError("La duración debe ser mayor a cero")

        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):
        costo = self.servicio.calcular_costo(self.horas)
        return costo