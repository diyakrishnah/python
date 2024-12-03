'''AUTHOR:Diya krishna
version1.1
date:30/11/2024'''
def count_upper_lower_case(string):
    upper_charector = 0
    lower_charector = 0
    for i in string:
        if i.isupper():
            upper_charector += 1
        elif i.islower():
            lower_charector += 1
    return upper_charector,lower_charector
string=input("enter a string:")
upper_charector,lower_charector=count_upper_lower_case(string)
print(upper_charector)
print(lower_charector)
