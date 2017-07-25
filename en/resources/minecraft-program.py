from mcpi.minecraft import Minecraft
from gpiozero import DigitalInputDevice
from time import sleep

mc = Minecraft.create()

mc.postToChat("Micromine bitcraft")

pin0 = DigitalInputDevice(17)
pin1 = DigitalInputDevice(27)

while True:
    sleep(0.1)
    pos = mc.player.getPos()
    if pin0.value == 1:
        pos.y = pos.y + 0.5
        mc.player.setPos(pos)
    if pin1.value == 1:
        pos.y = pos.y - 1
        mc.setBlock(pos, 0)
