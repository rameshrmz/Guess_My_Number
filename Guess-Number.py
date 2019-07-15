# Guess My Number between 1 and 100!!!

import random

#myNumber = [10,40,38,56,100,2,67,50]
#random_sel_myNumber = random.choice(myNumber)

print ("**********    GueSs iT    ***********")

print ("Guess My Number between 1 to 100. You have 6 lifes.\n")
print ("(Note: You can take clue, when you are close to my number. You can see clue only Once, but your life get reduce by one.)\n\n")

clue_ind = "N"
clue_over = "No"

random_sel_myNumber = random.randint(1,101)


for number in range(1,7):

	if clue_ind.upper() == "Y":
		clue_ind = "N"
		clue_over = "Yes"
		continue
	
	if number == 1:
		myNum = int(input("Guess My Number:"))
	elif number > 1 and number < 6:
		myNum = int(input("Guess My Number Again:"))
	else:
		myNum = int(input("Your Last Chance!!! Guess My Number:"))


	if myNum > random_sel_myNumber:
		diff = myNum - random_sel_myNumber
		if diff <= 3:
			print ("Very close to the Value. Keep Try!!! \n")
		#Clue
			if (clue_over == "No") and (number < 5) :
				clue_ind = input ("Want to see clue??? Y / N")
				if clue_ind.upper() == "Y":
					print ("Your Number > mine!!!\n")
		else:
			print ("Too High!!!" + "\n")
		continue

	elif myNum < random_sel_myNumber:
		diff = random_sel_myNumber - myNum
		if diff <= 3:
			print ("Very close to the Value. Keep Try!!! \n")
		#Clue
			if (clue_over == "No") and (number < 5) :
				clue_ind = input ("Want to see clue??? Y / N ")
				if clue_ind.upper() == "Y":
					print ("Your Number < mine!!!\n")

		else:
			print ("Too Low!!!" + "\n")
		continue

	else:
		print ("That's It!!!" + "\n")
		break


print ("Thanks for Playing!!! My Number is:", random_sel_myNumber)