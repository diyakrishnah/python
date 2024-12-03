'''AUTHOR:Diya krishna
DATE:3/12/24
version1.1'''
#Recursive function to multiply two positive numbers
def multiplication(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multiplication(n1,n2-1)
n1=int(input("Enter first number :"))
n2=int(input("Enter second number :"))
print("The produt of ",n1,"and",n2, "is ",multiplication(n1,n2))


