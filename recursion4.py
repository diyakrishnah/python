'''AUTHOR:Diya krishna
DATE:3/12/24
version1.1'''
#Recursive function to find the greatest common divisor of two positive numbers.
def greatest_common_divisor(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return greatest_common_divisor(n2,n1%n2)
n1=int(input("Enter first number :"))
n2=int(input("Enter second number :"))
print("The greatest common divisor of this numbers is ",greatest_common_divisor(n1,n2))