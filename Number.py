'''
DATE:15/10/2024
Python project to check the given number
is positive or not
 '''
Number=int(input("Enter a number:"))
if Number>0:
    print("The given number",Number,"is positive.")
elif Number<0:
    print("The given number",Number," is negative.")
else:
    print("The given number",Number,"is Zero")