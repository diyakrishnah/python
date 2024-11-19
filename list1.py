'''
AUTHOR:Diya krishna
PROGRAM TO REMOVE DUPLICATES FROM THE LIST
DATE:19/11/2024
'''
numbers=[1,2,3,2,8,1,7,8,]
unique_list=[]
for number in numbers:
    if number not in unique_list:
        unique_list.append(number)
print("The orginal list is ",numbers)
print(unique_list)
