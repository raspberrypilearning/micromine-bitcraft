## Buttons and pins
Now you need to finish your micro:bit program so that it turns the pins on and off when it's shaken or when the button is pressed.

- Go back to Mu and modify your program so that it turns the pins on `(1)` and off `(0)` when shaken and when button A is pressed:

	```python
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
    ```
	
            
- Now click **Flash** to transfer your program to your micro:bit.
- Test your program. The letter `A` should appear on the micro:bit LEDs when the button is pressed.

