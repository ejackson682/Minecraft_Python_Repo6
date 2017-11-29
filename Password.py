Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> zombies = int(input("Enter the number of zombies: "))
Enter the number of zombies: 15
>>> if zombies > 20:
	print("That's a lot of zombies.")

	
>>> if zombies > 20:
	print("That's a lot of zombies.")
	Enter the number of zombies: 22
	
SyntaxError: invalid syntax
>>> password = "cats"
>>> attempt = input("Please enter the password: ")
Please enter the password: cats
>>> if attempt == password:
	print("Password is correct")
	print("Program finished")

	
Password is correct
Program finished
>>> 
