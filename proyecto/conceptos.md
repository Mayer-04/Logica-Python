# Conceptos de MicroPython

## PWM

PWM permite simular señales analógicas utilizando señales digitales.
Útil para controlar dispositivos como motores, luces y otros componentes que requieren un control de potencia variable.

- crear un objeto PWM asociado a un pin específico.
- PWM es una técnica para controlar la potencia en dispositivos electrónicos.

### freq()

- freq(frecuency): Este método se utiliza para establecer la frecuencia de la señal PWM.
- frecuency: El valor de frecuencia en hertz (Hz).

```python
pwm.freq(1000)  # Establece la frecuencia a 1000 Hz
```

### duty()

Este método se utiliza para establecer el ciclo de trabajo (duty cycle) de la señal PWM, que es el porcentaje de tiempo que la señal está en estado alto (encendido) en un ciclo de la señal.

- duty(duty_cycle)
- duty_cycle: Un valor que puede variar típicamente entre 0 (0%) y 1023 (100%) en MicroPython.
- Un valor de 0 significa que el PWM está apagado todo el tiempo.
- Un valor de 1023 significa que está encendido todo el tiempo.

### deinit()

Este método se utiliza para desactivar el PWM y liberar el pin que estaba utilizando.

- Cuando ya no necesitas el PWM en ese pin, puedes llamar a deinit() para liberar el recurso.

```python
pwm.deinit()  # Desactiva el PWM y libera el pin
```
