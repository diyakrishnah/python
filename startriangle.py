'''AUTHOR :DIYA KRISHNA
DATE:19/11/2024'''
print("increasing triangle")
limit=int(input("Enter a limit :"))
for star1 in range(limit):
    for star2 in range(star1):
        print ("*",end=" ")
    print()
print("decreasing triangle")
for star1 in range(limit):
    for star2 in range(limit-star1):
        print ("*",end=" ")
    print()
print("hill pattern")
for star1 in range(limit):
    for star2 in range (limit-star1):
        print(" ",end=" ")
    for star3 in range((2*limit)-(2*star2)-1):
        print ("*",end=" ")
    print()
print("revers hill pattern")
for star1 in range(limit):
    for star2 in range (limit+star1):
        print(" ",end=" ")
    for star3 in range((2*limit)-(2*star1)-1):
        print ("*",end=" ")
    print()