'''
AUTHOR:DIYA KRISHNA
Date:15/10/2024
version:1.1
'''
number=int(input("enter a number:"))
sum=0
while number>0:
    reminder=number%10
    number=number//10
    sum=sum+reminder
print("sum is ",sum)