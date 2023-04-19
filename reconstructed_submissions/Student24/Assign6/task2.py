# @@@@@@@@@@@@
# CS1400 - MW1
# Assignment 6

# Import random
import random
 
# Define a variable to use for our loop
game = True
# Begin loop for our variable
while game:
	night = 0 # Number of nights to go up to 100,000
	oneElephant = 0 # Variable to hold number of nights zookeeper sees one elephant
	twoElephant = 0 #  Variable to hold number of nights zookeeper sees two elephants
# Begin loop for nightly checks
	while night < 100000:
		night += 1 # Increment number of nights
# Get random pen assignments for zookeeper and elephants
		custodian = random.randint(1, 6) 
		elephant1 = random.randint(1, 6) 
		elephant2 = random.randint(1, 6) 
# Keep track of how many nights he sees one or two elephants
		if custodian == elephant1 == elephant2:
			twoElephant += 1
		elif custodian == elephant1 or custodian == elephant2:
			oneElephant += 1
# Compare the number of nights of one elephant to the whole 100,000
	ratioOneElephant = float(oneElephant / 100000)
# Compare the number of nights of seeing two elephants to the number of nights he sees one
	ratioTwoElephant = float(twoElephant / oneElephant)
# Print the results
	print("The ratio of time there is at least one elephant in the pen the zookeeper checks is " + str(format(100 * ratioOneElephant, ".2f")) + "%.") 
	print("The ratio of time there is another elephant when the zookeeper checks and sees one already is " + str(format(100 * ratioTwoElephant, ".2f")) + "%.")
# Input from user to run again
	question = input(format("Would you like to play again? ")).lower()
	if question == "yes":
		game = True
	else:
		game = False
		print("Alright. Thank you for playing!")


		

