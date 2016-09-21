# Micromine bitcraft

Using Python you can use your micro:bit to help(or sabotage!) Steve in Minecraft. You are going to connect the pins on your micro:bit to the Raspberry Pi GPIO pins using some cables and crocodile clips; programs on the micro:bit and Raspberry Pi will make Steve shake in Minecraft when the micro:bit is shaken and blocks disappear and button A is pressed.

## Startin mu

1. Open `Mu` from the main menu under `Programming`.

1. A new window should open up that looks like this:

	![mu screenshot](images/screen1.png)

## Plugging in your micro:bit

The micro:bit has a micro USB port that you can use to connect it to your Raspberry Pi. This will provide a power *and* data connection.

1. Connect your Raspberry Pi to the micro:bit using a USB A-to-micro-B cable, as shown below:

	![usb setup](images/usb.png)

1. You'll know that the micro:bit has connected to your Raspberry Pi, because a dialogue box should pop up like the one below:

	![screen2](images/screen2.png)

1. This dialogue box might pop up a few times while you're playing with the micro:bit. You can simply click on `Cancel` when it does.

## Write a program to make your micro:bit angry

1. Click **New** and type the following code into the editor.

	```python
	from microbit import *
	
	while True:
        if accelerometer.current_gesture() == "shake":
            display.show(Image.ANGRY)
        else:
            display.show(Image.HAPPY)
    ```
                
1. Click the **Flash** icon on the menu to transfer your program on your micro:bit.

1. When the yellow light on the back of your micro:bit stops flashing your program will run and you should see a happy face on your micro:bit - until it’s shaken!

*Note: Any errors will be scrolled on your micro:bit’s leds. If you get an error check your code carefully. Capital letters are important True is different to true.*

## Buttons and pins
Now you need to finish your micro:bit program so that it turns the pins on and off when it's shaken or the button is pressed.

1. Go back to Mu and modify your program so that it turns the pins on (1) and off (0) when shaken and when button A is pressed.

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
            
1. Now click Flash to transfer your program on your micro:bit.
1. Test your program, A should appear on the screen when the button is pressed.

## Connect it to your Raspberry Pi
Next you will use jumper cables and crocodile clips to connect your micro:bit to the Raspberry Pi - you will connect 2 of the pins on the Raspberry Pi to the 0 and 1 pins on the micro:bit.

1. Connect the jumper cable to GPIO17 on the Raspberry Pi
1. Clip the crocodile clip to the end of the jumper cable
1. Clip the other end of the crocodile clip to pin0 on the micro:bit
1. Repeat to connect GPIO27 to pin1

	![](images/microbit-pi-pins-connect.png)
## Shake Steve in Minecraft

1. You now need to create your Minecraft program to shake Steve when the micro:bit is shaken and pin0 is set to 1.
1. Click Menu > Games > Minecraft: Pi Edition to run the game.
1. Click Start Game, then click Create New (or choose an existing one) to enter a world.
1. Press ESC to go back to the Minecraft menu but leave the game playing.
1. Open Python 3 (IDLE3) by clicking Menu > Programming > Python 3.
1. se File > New Window to create a new program and save it as ‘mc_micro.py’.
1. Type the following code into the program to import the modules you will need.

	```python
	from mcpi.minecraft import Minecraft
    from gpiozero import DigitalInputDevice
    from time import sleep
    ```

1. Underneath create a connection to Minecraft by typing:
	
	```python
	mc = Minecraft.create()
	```

1. Next, type the line of code that will post a message to the chat window:

	```python
	mc.postToChat("Micromine bitcraft")
	```

1. Save and run your program by clicking **Run** and **Run Module**. You should see your message appear in the Minecraft chat window.

	*Note: Any errors will be displayed in the Python Shell in red. If you get an error check your code carefully. The message disappears from Minecraft after 10 seconds, if you miss it, re-run your program.*

1. Next, create a pin which is connected to Pi GPIO 17 and micro:bit pin 0 by typing:

	```python
	pin0 = DigitalInputDevice(17)
	```

1. Then create a loop which constants gets Steve’s position:

	```python
	while True:
        sleep(0.1)
        pos = mc.player.getPos()
        if pin0.value == 1:
            pos.y = pos.y + 0.5
            mc.player.setPos(pos)
     ```   
        
    If pin0 is on (1) it adds 0.5 to Steve’s height (y).

1. Run your program by clicking Run > Run Module. Shake your micro:bit and Steve will be shaken in Minecraft.

## Make blocks disappear 
When the micro:bit A button is pressed your program should also make blocks disappear.

1. Underneath the lines of code you have written to connect GPIO 17 to micro:bit pin 0, add another line of code to connect GPIO 27 to pin 1 by typing:

	```python
    pin1 = DigitalInputDevice(27)
    ```
1. At the bottom of your program, inside the while True loop add the code so that if pin1 is on (1) it sets the block below Steve to AIR (0):

	```python
    if pin1.value == 1:
        pos.y = pos.y - 1
        mc.setBlock(pos, 0)
    ```    

1. Run your program, press the A button and see the blocks below Steve disappear.

## What next?
- Can you modify the micro:bit and Minecraft program so that Button B makes blocks appear under Steve?
- Modify the Minecraft program to make different block types appear like TNT (46) or Melon (103)

