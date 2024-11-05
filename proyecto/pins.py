from machine import Pin

"""
GPIO: pines en microcontroladores y placas de desarrollo
que pueden ser configurados para funcionar como entradas o salidas según sea necesario.
"""

p0 = Pin(0, Pin.OUT)  # Crea un pin de salida en GPIO0.
p0.on()  # Establece el pin en "encendido" (nivel alto).
p0.off()  # Establece el pin en "apagado" (nivel bajo).
p0.value(1)  # Establece el pin en "encendido" o nivel alto (equivalente a on()).

p2 = Pin(2, Pin.IN)  # Crea un pin de entrada en GPIO2.
print(p2.value())  # Obtiene el valor del pin, 0 (bajo) o 1 (alto).

p4 = Pin(
    4, Pin.IN, Pin.PULL_UP
)  # Crea un pin de entrada en GPIO4 y activa una resistencia de pull-up interna.
p5 = Pin(
    5, Pin.OUT, value=1
)  # Crea un pin de salida en GPIO5 y lo establece en nivel alto desde la creación.
p6 = Pin(
    6, Pin.OUT, drive=Pin.DRIVE_3
)  # Crea un pin de salida en GPIO6 con la máxima potencia de salida.
