import ventana1
from gpiozero import LED

led1 = LED(13)
led = LED(17)
led.on()
led1.on()

ventana1.mostrar_ventana()