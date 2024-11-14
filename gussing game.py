import random
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myno = random.randint(smaller, larger)
count = 0
while True:
	count+=1
	usernumber= int(input("enter a guess"))
	if usernumber<myno:
		print("too small")
	elif usernumber>myno:
		print("too large")
	else:
		print("congrats!you win")
		break