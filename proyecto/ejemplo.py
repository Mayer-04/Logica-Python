from machine import Pin, PWM
import time


# Motor A (OUT1 y OUT2)
IN1 = Pin(5, Pin.OUT)
IN2 = Pin(4, Pin.OUT)
ENA = PWM(Pin(18), freq=1000)

# Motor B (OUT3 y OUT4)
# !NOTE: Por definir.
IN3 = Pin(6, Pin.OUT)
IN4 = Pin(7, Pin.OUT)
ENB = PWM(Pin(19), freq=1000)


def setup():
    print("Configuración inicial del programa")


def set_motor_speed(motor_pwm: PWM, speed: int) -> None:
    """
    Establece la velocidad PWM de los motores.

    Párametros:
    - motor_pwm: El objeto PWM que controla el motor.
    - Un valor entre 0 y 1023 que representa el ciclo de trabajo PWM.
    """
    motor_pwm.duty(speed)


def set_pin_value(pin: Pin, value: int) -> None:
    """
    Establece el valor especificado en un pin GPIO.

    Parámetros:
    - pin: El pin GPIO que se va a controlar.
    - valor: un número entero (0 o 1) para establecer el pin bajo o alto.
    """
    pin.value(value)


def motor_stop():
    # !NOTE: Podemos poner en 0 en los pines de control de los motores.
    set_motor_speed(ENA, 0)
    set_motor_speed(ENB, 0)


def move_forward(speed: int = 512) -> None:
    # Configura los pines de control de los motores.
    """
    Mueve el vehículo hacia adelante.

    Parámetros:
    - speed: Un valor entre 0 y 1023 que representa el ciclo de trabajo PWM para los motores.
    Por defecto es 512 (50%).
    """
    set_pin_value(IN1, 1)  # IN1.on()
    set_pin_value(IN2, 0)  # IN2.off()
    set_pin_value(IN3, 1)  # IN3.on()
    set_pin_value(IN4, 0)  # IN4.off()

    # Establece la velocidad PWM de los motores.
    set_motor_speed(ENA, speed)
    set_motor_speed(ENB, speed)


def move_backward(speed: int = 512) -> None:
    IN1.off()  # set_pin_value(IN1, 0)
    IN2.on()  # set_pin_value(IN2, 1)
    IN3.off()  # set_pin_value(IN3, 0)
    IN4.on()  # set_pin_value(IN4, 1)

    # Establece la velocidad PWM de los motores.
    set_motor_speed(ENA, speed)
    set_motor_speed(ENB, speed)


while True:
    break
