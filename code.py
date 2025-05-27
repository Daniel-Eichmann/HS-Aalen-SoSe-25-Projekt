import time
import digitalio
import board
from adafruit_debouncer import Debouncer

def setup_button(pin):
    io = digitalio.DigitalInOut(pin)
    io.direction = digitalio.Direction.INPUT
    io.pull = digitalio.Pull.DOWN
    return Debouncer(io)

redbutton = setup_button(board.GP16)
bluebutton = setup_button(board.GP17)
yellowbutton = setup_button(board.GP18)
whitebutton = setup_button(board.GP19)

while True:
    redbutton.update()
    bluebutton.update()
    yellowbutton.update()
    whitebutton.update()

    print("Red button is currently pressed:", redbutton.value)