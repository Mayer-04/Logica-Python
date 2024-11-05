from machine import Pin, PWM
import time

"""
GPIO: Pines configurables en microcontroladores que pueden actuar como entradas o salidas.

- Ejemplo de un PIN de salida en el GPIO 5: IN1 = Pin(5, Pin.OUT).

Definir un PIN de salida con un valor inicial:

IN1 = Pin(5, Pin.OUT, value=1)
"""


# Pines de la ESP32 conectados al driver L298N.
# Definimos `constantes` para los pines de control del motor.
IN1 = Pin(5, Pin.OUT)  # Pin IN1 del L298N para control del motor
IN2 = Pin(4, Pin.OUT)  # Pin IN2 del L298N para control del motor

# !NOTE: Faltan por definir 2 pines para motor B.
# Motor 3 y 4 en el OUT3 y OUT4.
IN3 = Pin(5, Pin.OUT)
IN4 = Pin(5, Pin.OUT)

# Configuramos el estado inicial de los pines
IN1.on()  # Activa el pin (señal alta)
IN2.off()  # Desactiva el pin (señal baja)

# Alternativa para activar o desactivar los pines
IN1.value(1)  # Activa el pin (igual que on())
IN2.value(0)  # Desactiva el pin (igual que off())

# Configuración del PWM en el pin ENA para controlar la velocidad del motor.
ENA = PWM(Pin(18), freq=1000)  # Frecuencia inicial de 1000 Hz en el pin ENA

"""
Configuración del PWM:
- Se puede definir la `frecuencia` de dos maneras:
  1. Al crear el PWM: ENA = PWM(Pin(18), freq=1000)
  2. Después de crear el PWM: ENA.freq(1000)

- Se puede definir el `duty` (ciclo de trabajo) como parámetro adicional:
  ENA = PWM(Pin(18), freq=1000, duty=256)

Nota: `duty` varía de 0 a 1023 (0 = apagado, 1023 = máxima velocidad).
"""

# Verificar el ciclo de trabajo actual, con un valor inicial de 512 (50%).
duty = ENA.duty()

# Establecer el ciclo de trabajo al 25% (256/1023).
ENA.duty(256)

# Apagar el PWM y liberar el pin.
# Recomendado cuando ya no se requiere el PIN.
ENA.deinit()


# Función de configuración para ejecutar al iniciar el programa.
def setup():
    print("Configurando el programa...")

    # TODO: Se deben detener los motores en su estado inicial.
    pass


def loop():
    pass


while True:
    # loop()
    break


# * Funciones para controlar el movimiento del vehículo.
def set_motor_speed(motor_pwm: PWM, speed: int) -> None:
    """
    Establece la velocidad PWM de los motores.

    Párametros:
    - motor_pwm: El objeto PWM que controla el motor.
    - Un valor entre 0 y 1023 que representa el ciclo de trabajo PWM.
    """
    motor_pwm.duty(speed)


def move_forward():
    """Mueve el vehículo hacia adelante."""
    IN1.on()
    IN2.off()
    # TODO: Usar la función set_speed
    ENA.duty(1023)  # Velocidad máxima


def move_backward():
    """Mueve el vehículo hacia atrás."""
    pass


def motor_stop():
    """Detiene temporalmente el motor sin desactivar el PWM."""
    # Temporiza el motor sin necesidad de reiniciar el PWM.
    # ena.duty(0)
    pass


def turn_left():
    """Gira el vehículo hacia la izquierda."""
    pass


def turn_right():
    """Gira el vehículo hacia la derecha."""
    pass
