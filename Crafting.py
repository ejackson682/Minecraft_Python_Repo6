Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> x = 6
>>> y = 5
>>> z = 28
>>> blockType = 103
>>> up = 1
>>> mc.setBlock(x, y, z, blockType)
>>> mc.setBlock(x,y + up, z, blockType)
>>>
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
width = 10
height = 5
length = 6
blockType = 4
air = 0
mc.setBlocks( x, y, z, x + width, y + height, z + length, blockType)

