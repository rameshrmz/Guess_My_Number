# Guess My Number between 1 and 100!!!

import random

#myNumber = [10,40,38,56,100,2,67,50]
#random_sel_myNumber = random.choice(myNumber)

random_sel_myNumber = random.randint(1,101)


for number in [1,2,3,4,5]:
	
	if number == 1:
		myNum = int(input("Guess My Number:"))
	elif number > 1 and number < 5:
		myNum = int(input("Guess My Number Again:"))
	else:
		myNum = int(input("Your Last Chance!!! Guess My Number:"))

	if myNum > random_sel_myNumber:
		print ("Too High!!!" + "\n")
		continue
	elif myNum < random_sel_myNumber:
		print ("Too Low!!!" + "\n")
		continue
	else:
		print ("That's It!!!" + "\n")
		break

print ("Thanks for Playing!!! My Number is:")
print (random_sel_myNumber)