'''Author:Diya krishna
version 1.1
DATE:3/12/2024'''
#program to define a module to find fibonacci numbers and import the mode to another program
def generate_fibonacci(n):
    sequence=[]
    first_number,second_number=0,1
    for i in range(n):
        sequence.append(first_number)
        first_number,second_number=second_number,first_number+second_number
    return sequence
print(generate_fibonacci(10))