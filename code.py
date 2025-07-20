
import board
import digitalio
import time
import usb_cdc

buttons = {
    "w": digitalio.DigitalInOut(board.GP5),
    "s": digitalio.DigitalInOut(board.GP7),
    "a": digitalio.DigitalInOut(board.GP10),
    "d": digitalio.DigitalInOut(board.GP12),
    "escape": digitalio.DigitalInOut(board.GP15),
    "enter": digitalio.DigitalInOut(board.GP16)
}

for btn in buttons.values():
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.GP1)
led.direction = digitalio.Direction.OUTPUT
led.value = True

while True:
    pressed_keys = [key for key, btn in buttons.items() if not btn.value]
    
    if pressed_keys:
        line = ",".join(pressed_keys) + "\n"
        usb_cdc.data.write(line.encode())
    
    time.sleep(0.05)