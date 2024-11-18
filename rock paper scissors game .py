'''ROCK PAPER SCISSOR '''
import random
choice=["paper","rock","scissors"]
computerscore=0
userscore=0
while True :
	guess=random.choice(choice)
	print(choice)
	userinput=input("Enter a choice:,or enter 'quit' to exit :")
	if userinput=='quit':
		print("Thankyou for playing")
		break
		print("computer guess was ",guess)
	if userinput==guess:
		print("it was a tie")
	else:
		if (userinput=="rock"and guess=="paper")or (userinput=="paper" and guess =="scissor")or (userinput=="scissor" and guess=="rock"):
			computerscore+=1
			print(f"computer choise is ",guess)
			print("computer win!")
			print("computer score:",computerscore)
		else:
			userscore+=1
			print("Congrats ! You Win")
			print("your score :", userscore)