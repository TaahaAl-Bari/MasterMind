import random
correctanswer = ''

for i in range (4):
 tempchart = str(random.randint(0,9))
 correctanswer = correctanswer + tempchart
guess = ''
attempts = 0
while guess !="q":
 guess = input("Please enter a 4 digit number or press q to quit :")
 
 if guess.isnumeric()and len(guess) == 4:
     numcorrect = 0

for i in range(0,3):
 if guess[i] == correctanswer[i]:
     numcorrect += 1
 
if(choice == correctanswer):
 print("Well done... it took you ”+ str(attempts)")
else:
 print("That’s not right. You have guessed ”+ str (numcorrect) + ")
 attempts += 1
