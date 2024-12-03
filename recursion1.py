'''AUTHOR:Diya krishna
DATE:3/12/24
version1.1'''
#factorial of a number
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter a number:"))
print("factorial of ",n,"is",factorial(n))
