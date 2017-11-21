Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> blockType = # Add input() function here
SyntaxError: invalid syntax
>>> pos = mc.player.getTilePos()
>>> x = pos.x
>>> y = pos.y
>>> z = pos.z
>>> mc.setBlock(x, y, z, blockType)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    mc.setBlock(x, y, z, blockType)
NameError: name 'blockType' is not defined
>>> blockType = 100
>>> mc.setBlock(x, y, z, blockType)
>>> blockType = int(input("stone: "))
stone: 
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    blockType = int(input("stone: "))
ValueError: invalid literal for int() with base 10: ''
>>> try:
	noOfSunglasses = int(input("How many sunglasses do you own? "))
	except
	
SyntaxError: invalid syntax
>>> try:
	noOfSunGlasses = int(input("How many sunglasses do you own? "))
	except:
		
SyntaxError: invalid syntax
>>> print("Invalid input: please enter a nu,ber)
      
SyntaxError: EOL while scanning string literal
>>> try:
	blockType = int(input("stone: "))
	mc.setBlock(x, y, z, blockType)
	except:
		
SyntaxError: invalid syntax
>>> except = 1
SyntaxError: invalid syntax
>>> 
