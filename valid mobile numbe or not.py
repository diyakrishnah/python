'''AUTHOR:Diya krishna
version1.1
date:30/11/2024'''
def phone_number(phone):
    if len(phone)==10 and phone[0] in "789":
        print("it's a phone number")
    else:
        print("it is not a phone number")
phone=input("Enter a valid phone number: " )
phone_number(phone)