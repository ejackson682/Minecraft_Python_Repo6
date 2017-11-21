Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from mcpi.mibecraft import Minecraft
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from mcpi.mibecraft import Minecraft
ImportError: No module named 'mcpi.mibecraft'
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> pos = mc.player.getTilepos()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    pos = mc.player.getTilepos()
AttributeError: 'CmdPlayer' object has no attribute 'getTilepos'
>>> pos = mc.player.getTilePos()
>>> x = pos.x
>>> y = pos.y
>>> z = pos.z
>>> height = 2
>>> blockType = 1
>>> # Spire sides should be same as height
>>> sideHeight = height
>>> mc.setBlocks(x + 1, y, z + 1, x + 3, y + sideHeight - 1, z + 3, blockType)
>>> #Spire point: should be two times the height
>>> pointHeight = 4
>>> mc.setBlocks(x + 2, y, z + 2, x + 2, y + pointHeight - 1, z + 2, blockType)
>>> # Spire base: should be half the height
>>> baseHeight = 1
>>> mc.setBlocks(x, y, z, x +4, y + baseHeight - 1, z + 4, blockType)
>>> wheat = 4 ** 3
>>> mooshroom = 5 * 2 - 1 + 4 / 2
>>> zombiePigman = 6 * (3 - 2)
>>> sheep = 6
>>> sheep = sheep + 5
>>> import random
>>> diceValue = random.randint(1, 6)
>>> import random
>>> score = 0
>>> score += random.randint(0, 99)
>>> points = random.randint(-99, 99)
>>> 
