from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 10
y = 11
z = 12
blockType = 57
blockType = 6
gift = mc.getBlock(x, y, z)
diamond = 57
sapling = 6
if diamond:
    print("Thanks for the diamond")
elif sapling:
    print("Thanks for the sapling")
else:
    mc.postToChat("Bring a gift to " + str(x) + "," + str(y) + "," +str(z))
