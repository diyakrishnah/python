'''
AUTHOR:DIYA KRISHNA
Date:15/10/2024
version:1.1
python program to generate n odd numbers
'''
limit=int(input("Enter a number:"))
odd_number=1
count=0
while count<limit:
    print(odd_number,"\t",end="")
    count+=1
    odd_number+=2