# This is my first attempt at making a text based "choose your own adventure" game.
# My goal for this game is to allow the user to make choices about their journey based on input
# Another goal was to have a global variable, the key, and experiment with how the output would change if the user made the 
# same choice with a different global variable value. 


from sys import exit #allows me to use the exit function to quit python when game ends

# This function will do all the choice formatting for me. All I need to do is type in the choices as str. 
def formatting(x,y):
	return raw_input("A: %s \nB: %s \n" %(x,y)).lower()
def oak(): 
	print "You are at Oak's house.\nYou see a locked box and and open door.\nWhat do you do?"
	choice = formatting("Leave", "Open the box.")

	if choice == "a":
		print "You exit the house."
		front_yard()
	elif choice == "b" and haskey == 0: 
		print "This box is locked! You need a key to open it." #covers user with no key
		oak() 
	elif choice =="b" and haskey == 1:
		print "The key fits!\nYou open the lid and find 20,0000 lbs of gold!!!\nYou win!!!"
		exit(0) # user wins the game, exit out of python
	else:
		print "Your choice doesn't make any sense.\nTry again." #covers all other user input

def front_yard(): 
	global haskey #global is needed to allow glabal variable to be modified from within a function
	print "You are standing in the front yard.\nThere is a mailbox and not much else to see here."
	print "What do you want to do?"

	choice = formatting("Go back inside", "Open up the mailbox")

	if choice == "a":
		oak()
	elif choice == "b" and haskey == 0:
		print "You found the key!\nProfessor Oak must have left it here for you."
		haskey = 1 #set haskey value to 1 to signify you found and currently possess the key
		front_yard()
	elif choice == "b" and haskey == 1: #covers user tring to go back in mailbox after taking key
		print "This mailbox is empty. You already took the key"
		front_yard()
	else:
		print "I don't understand your choice.\nTry again." #covers all other user input
		front_yard()

def start(): 
	oak()


haskey = 0 

start()


