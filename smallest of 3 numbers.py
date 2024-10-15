'''
AYTHOR:DIYA KRISHNA
DATE:15/10/2024
VERSION:1.1
'''
a=int(input("Enter a number(a):"))
print("number(b) must not equal to (a)")
b=int(input("Enter a number(b):"))
print("number(c) must  not equal to (b)and(a)")
c=int(input("Enter a number(c):"))
if a<b and a<c:
    print("(a):",a,"is the smallest number.")
elif b<a and b<c:
    print("(b):",b,"is the smallest number.")
else:
    print("(c):",c,"is the smallest number.")