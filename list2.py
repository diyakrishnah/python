'''
AUTHOR:DIYAKRISHNA
DATE:19/11/2024
combining and finding odd ,even list from 2 list.
'''
list1=[]
list2=[]
list1_size=int(input("Enter list 1 size:"))
print("Enter the elements of the list 1 :")
for i in range (list1_size):
    list1.append(int(input()))
list2_size=int(input("Enter list 2 size:"))
print("Enter the elements of list 2:")
for i in range (list2_size):
    list2.append(int(input()))
print(list1,list2)
combine=list1+list2
print(combine)
even_list=[]
odd_list=[]
for i in combine:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("even numbers in the list is ",even_list)
print("odd numbers in the lis is ",odd_list)
even_list.sort()
odd_list.sort()
merge=even_list+odd_list
print("combination of odd and even list is ",merge)