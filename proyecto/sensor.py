from machine import Pin, time_pulse_us
import time

"""
* SENSOR ULTRASONICO HC-SR04
-----------------------------
El sensor de ultrasonido tiene dos pines importantes:
- Trig: Para disparar la señal de ultrasonido.
- Echo: Para recibir la señal de rebote.
"""

# Constantes para la configuración de los pines
ECHO_PIN = 18  # GPIO18
TRIG_PIN = 5  # GPIO5

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)


trig_pin.value()


"""
* time_pulse_us():
- Mide el tiempo que un pin de entrada permanece en un estado específico (alto o bajo) en microsegundos.

time_pulse_us(pin, pulse_level, timeout_us)

- pin: es el pin que se va a medir (debe estar configurado como entrada).
- pulse_level: es el estado lógico que queremos medir (1 para alto, 0 para bajo).
- timeout_us: es el tiempo máximo en microsegundos que la función esperará antes de salir si el pulso no se completa


Retorna la duración del pulso en microsegundos como un valor entero.

Distancia= 
2
Tiempo medido (us)×Velocidad del sonido
"""
time_pulse_us()
