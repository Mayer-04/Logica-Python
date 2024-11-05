import time

time.sleep(1)  # sleep for 1 second
time.sleep_ms(500)  # sleep for 500 milliseconds
time.sleep_us(10)  # sleep for 10 microseconds
start = time.ticks_ms()  # get millisecond counter
print(start)


def set_servo_angle(angle: int) -> None:
    """Ajusta el ángulo del servo de 0 a 180 grados."""
    if angle < 0 or angle > 180:
        raise ValueError("El ángulo debe estar entre 0 y 180")

    duty_cycle = int((angle / 180) * 1023 + 25)
    # TODO: Usar la función set_speed
    ENA.duty(duty_cycle)
