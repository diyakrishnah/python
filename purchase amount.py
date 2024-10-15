'''
AUTHOR:Diya Krishna .M
DATE:15/10/2024
VERSION:1.1
'''
Amount = int(input("Enter a Purchase amount:"))
if Amount > 500:
    discount = Amount*0.20
    finalamount1= Amount-discount
    print("Final amount is:", finalamount1)
elif Amount>=200 and Amount<=500:
    discount2 =Amount*0.10
    finalamount2=Amount-discount2
    print("Final amount is:", finalamount2)
else:
    print("final amount=",Amount,)
