direc = 0
step = 0
""" TODO
1. Think of game name
2. Think of items
3. Think of characters
4. Think of EndGame
"""

print "Welcome to !!!!!!"
print "In this game, you can either go Front, Right, Left, and Back."
print "This game runs on the world's fastest graphics processor, the human brain."
print "Imagine away!"


#Start
label: direction
while True:
	a = raw_input("Which direction do you desire to go?")
	if a == "Front":
		direc = 1
		step = step + 1
		break
	elif a == "Right":
		direc = 2
		step = step + 1 
		break
	elif a == "Left":
		direc = 3
		break
	elif a == "Back":
		print "You can't go back!"
	else:
		print "I don't know what %s means!" (a)




if step == 1:
	
