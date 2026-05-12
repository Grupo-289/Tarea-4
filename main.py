from modelos.cliente import Cliente
from modelos.reserva import Reserva

from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import Asesoria

from logs import registrar_log

try:

    cliente1 = Cliente("Oscar", "oscar@gmail.com")

    servicio1 = ReservaSala("Sala VIP", 50000)

    reserva1 = Reserva(cliente1, servicio1, 3)

    reserva1.confirmar()

    print(reserva1.procesar())

except Exception as e:

    registrar_log(str(e))

    print("Error:", e)

finally:
    print("Sistema ejecutado correctamente")
    