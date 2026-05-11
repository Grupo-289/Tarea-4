from modelos.cliente import Cliente
from modelos.reserva import Reserva

from modelos.servicios.reserva_sala import ReservaSala
from modelos.servicios.alquiler_equipo import AlquilerEquipo
from modelos.servicios.asesoria import Asesoria

from utilidades.logger import registrar_log

clientes = []
reservas = []

try:

    cliente1 = Cliente("Oscar", "oscar@gmail.com", "1234567")
    clientes.append(cliente1)

except Exception as e:

    registrar_log(str(e))

try:

    cliente2 = Cliente("", "correo_malo", "12")
    clientes.append(cliente2)

except Exception as e:

    registrar_log(str(e))

try:

    servicio1 = ReservaSala("Sala VIP", 100000)

    reserva1 = Reserva(cliente1, servicio1, 3)

    print(reserva1.procesar())

except Exception as e:

    registrar_log(str(e))

try:

    servicio2 = Asesoria("Asesoría IA", 150000)

    reserva2 = Reserva(cliente1, servicio2, -2)

    print(reserva2.procesar())

except Exception as e:

    registrar_log(str(e))

finally:
    print("Sistema ejecutado correctamente") #prueba de commit
    