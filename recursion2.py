'''AUTHOR:Diya krishna
DATE:3/12/24
version1.1'''
#recursion function to add two positive numbers
def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)
n1=int(input("Enter first number :"))
n2=int(input("Enter second number :"))
print("The addition of this numbers are",add_numbers(n1,n2))