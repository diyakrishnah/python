'''AUTHOR:Diya krishna
version1.1
date:30/11/2024'''
first_side=int(input("Enter the length of the first side:"))
second_side=int(input("Enter the length of the second side:"))
third_side=int(input("Enter the length of the third side:"))
def right_angled_triangle(first_side,second_side,third_side):
    list=[first_side,second_side,third_side]
    list.sort()
    if list[2]**2==list[1]**2+list[0]**2:
        return True
    return False
if right_angled_triangle(first_side,second_side,third_side):
    print("The given sides are a part of a right angled triangle")
else:
    print("The given sides are not a part of a right angled triangle")
