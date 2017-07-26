## Write a program to make your micro:bit angry

- Click **New** and type the following code into the editor:

	```python
	from microbit import *
	
	while True:
        if accelerometer.current_gesture() == "shake":
            display.show(Image.ANGRY)
        else:
            display.show(Image.HAPPY)
    ```
    
    Here you are using a `while True:` loop that will repeat the code inside it until you quit the program. Inside the loop, you are setting an `if else` condition: if the accelerometer on the micro:bit detects shaking, then it will display an angry face on the micro:bit LEDs. Otherwise, it will show a happy face.
                
- Click the **Flash** icon on the menu to transfer your program to your micro:bit.

- When the yellow light on the back of your micro:bit stops flashing, your program will run and you should see a happy face on your micro:bit - until it’s shaken!

**Note: Any errors will be scrolled on your micro:bit’s LEDs. If you get an error, check your code carefully. Capital letters are important: `True` is different from `true`.**

