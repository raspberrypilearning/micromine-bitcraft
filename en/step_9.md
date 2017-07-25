## Shake Steve in Minecraft

You now need to create your Minecraft program to shake Steve. To do this you will need to create another Python program, this time using Python 3 (IDLE3).

- First, open Minecraft Pi on the Raspberry Pi by clicking on **Menu**, **Games**, and **Minecraft: Pi Edition** to run the game.
- Click **Start Game**, then click **Create New** (or choose an existing one) to enter a world.
- Press **ESC** to go back to the Minecraft menu while leaving the game playing.
- Open Python 3 (IDLE3) from the Programming menu.
- Click on **File** and **New Window** to create a new program and save it as `mc_micro.py`.
- Start your program by importing all the modules you will need:

	```python
	from mcpi.minecraft import Minecraft
    from gpiozero import DigitalInputDevice
    from time import sleep
    ```
    Here you are using three different modules: one to connect to Minecraft Pi, one to program the GPIO pins, and one to add pauses or sleeps.

- Underneath, create a connection to Minecraft by typing:
	
	```python
	mc = Minecraft.create()
	```

- Next, type the line of code that will post a message to the chat window:

	```python
	mc.postToChat("Micromine bitcraft")
	```
	This will let you know that your program is working. If you don't see this message when you run your program, then you will know something is wrong.

- Save and run your program by clicking `Run` and `Run Module`. You should see your message appear in the Minecraft chat window.

	**Note: Any errors will be displayed in the Python shell in red. If you get an error, check your code carefully. The message disappears from Minecraft after ten seconds: if you miss it, re-run your program.**

- Next, create a pin which is connected to GPIO 17 on the Raspberry Pi and pin 0 on the micro:bit by typing:

	```python
	pin0 = DigitalInputDevice(17)
	```

- Then create a `while True:` loop which repeatedly gets Steve’s position:

	```python
	while True:
        sleep(0.1)
        pos = mc.player.getPos()
        if pin0.value == 1:
            pos.y = pos.y + 0.5
            mc.player.setPos(pos)
     ```   
        
    After getting Steve's position, if `pin0` is detected as being on or `(1)` then the code instructs Minecraft to add `0.5` to Steve’s height on the `(y)` coordinate. This will look like Steve is moving. 

- Run your program by clicking **Run** and **Run Module**. Shake your micro:bit and Steve will be shaken in Minecraft.

