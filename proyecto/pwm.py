from machine import Pin, PWM

# crea un objeto PWM en el pin especificado
pwm0 = PWM(Pin(0), freq=5000, duty_u16=32768)

# obtiene la frecuencia actual
freq = pwm0.freq()

# establece la frecuencia de PWM de 1Hz a 40MHz
pwm0.freq(1000)

# obtiene el ciclo de trabajo actual, rango de 0-1023 (por defecto 512, 50%)
duty = pwm0.duty()

# establece el ciclo de trabajo de 0 a 1023 como una proporción duty/1023, (ahora 25%)
# `duty` es un valor entre 0 y 1023 (0 = apagado, 1023 = máxima velocidad).
pwm0.duty(256)

# obtiene el ciclo de trabajo actual, rango de 0-65535
duty_u16 = pwm0.duty_u16()

# establece el ciclo de trabajo de 0 a 65535 como una proporción duty_u16/65535, (ahora 75%)
pwm0.duty_u16(2**16 * 3 // 4)

# obtiene el ancho de pulso actual en nanosegundos
duty_ns = pwm0.duty_ns()

# establece el ancho de pulso en nanosegundos de 0 a 1_000_000_000/freq, (ahora 25%)
pwm0.duty_ns(250_000)

# apaga el PWM en el pin
pwm0.deinit()

# crea y configura un nuevo PWM en el pin 2 en una sola línea
pwm2 = PWM(Pin(2), freq=20000, duty=512)

# muestra el objeto pwm2 con sus parámetros actuales
print(pwm2)
