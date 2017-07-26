from microbit import *

while True:
    if accelerometer.current_gesture() == "shake":
        display.show(Image.ANGRY)
        pin0.write_digital(1)
    elif button_a.is_pressed():
        display.show("A")
        pin1.write_digital(1)
    else:
        display.show(Image.HAPPY)
        pin0.write_digital(0)
        pin1.write_digital(0)
