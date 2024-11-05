from machine import Pin, time_pulse_us
import time

"""
* SENSOR ULTRASONICO HC-SR04
-----------------------------
El sensor de ultrasonido tiene dos pines importantes:
- Trig: para disparar la señal de ultrasonido.
- Echo: para recibir la señal de rebote.
"""

# Configuración de los pines
ECHO_PIN = 18  # GPIO18
TRIG_PIN = 5  # GPIO5

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)


trig_pin.value()