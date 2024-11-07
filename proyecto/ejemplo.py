from machine import Pin, PWM
import time


# Constantes
PWM_FREQUENCY = 1000


# Motor A (OUT1 y OUT2).
in1 = Pin(5, Pin.OUT)
in2 = Pin(4, Pin.OUT)
# Controla la velocidad del Motor A usando PWM con una frecuencia de 1000 Hz.
ena = PWM(Pin(18), freq=PWM_FREQUENCY)

# Motor B (OUT3 y OUT4).
# !NOTE: Por definir.
in3 = Pin(6, Pin.OUT)
in4 = Pin(7, Pin.OUT)
enb = PWM(Pin(19), freq=PWM_FREQUENCY)


"""
NOTAS:

* Frecuencia de PWM:
- Una frecuencia de 1000 Hz significa que el ciclo de "encendido-apagado" se repite 1000 veces por segundo.
- Permite que el motor reciba impulsos eléctricos tan rápido que el movimiento es suave y eficiente.
- Una frecuencia adecuada mejora la estabilidad, la eficiencia, y reduce ruidos y calentamiento.
"""


def set_motor_speed(motor_pwm: PWM, speed: int) -> None:
    """
    Ajusta la velocidad PWM de los motores.

    Párametros:
    - motor_pwm: El objeto PWM que controla el motor.
    - speed: Un valor entre 0 y 1023 que representa el ciclo de trabajo PWM.
    """
    motor_pwm.duty(speed)


def set_pin_value(pin: Pin, value: int) -> None:
    """
    Establece el valor especificado en un pin GPIO.

    Parámetros:
    - pin: El pin GPIO a controlar.
    - value: Un número entero (0 o 1) para establecer el pin bajo o alto.
    """
    pin.value(value)


def motor_stop():
    """
    Detiene ambos motores al establecer su velocidad PWM a cero.

    Esta función asegura que los motores conectados a los controladores PWM
    no se muevan al poner el ciclo de trabajo PWM a 0.
    """
    set_motor_speed(ena, 0)
    set_motor_speed(enb, 0)


def move_forward(speed: int = 512) -> None:
    """
    Mueve el vehículo hacia adelante.

    Parámetros:
    - speed: Ciclo de trabajo PWM para los motores.
    Por defecto es 512 (50%).
    """
    set_pin_value(in1, 1)  # in1.on()
    set_pin_value(in2, 0)  # in2.off()
    set_pin_value(in3, 1)  # in3.on()
    set_pin_value(in4, 0)  # in4.off()

    # Establece la velocidad PWM de los motores.
    set_motor_speed(ena, speed)
    set_motor_speed(enb, speed)


def move_backward(speed: int = 512) -> None:
    set_pin_value(in1, 0)  # in1.off()
    set_pin_value(in2, 1)  # in2.on()
    set_pin_value(in3, 0)  # in3.off()
    set_pin_value(in4, 1)  # in4.on()

    # Establece la velocidad PWM de los motores.
    set_motor_speed(ena, speed)
    set_motor_speed(enb, speed)


# Configuración inicial del programa
def setup() -> None:
    print("Configuración inicial del programa...")
    # Asegura que ambos motores estén detenidos al inicio
    motor_stop()

    time.sleep(2)

    print("Motores listos y detenidos")
    # Llama a la secuencia de prueba principal
    loop()


# Bucle principal de prueba
def loop():
    try:
        while True:
            print("Moviendo hacia adelante")
            move_forward()  # Por defecto la celocidad es 50%
            time.sleep(2)  # Mueve hacia adelante durante 2 segundos

            print("Deteniendo")
            motor_stop()
            time.sleep(1)  # Pausa de 1 segundo

            print("Moviendo hacia atrás")
            move_backward()  # Por defecto la celocidad es 50%
            time.sleep(2)  # Mueve hacia atrás durante 2 segundos

            print("Deteniendo")
            motor_stop()
            time.sleep(1)  # Pausa de 1 segundo

    except KeyboardInterrupt:
        print("Deteniendo manualmente")
        motor_stop()


setup()
