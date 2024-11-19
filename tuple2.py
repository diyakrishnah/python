'''
AUTHOR:Diya krishna
DATE:19/11/2024
'''
inventory=[
    ("laptop",5,60000.00),
    ("Headphone",15,500.00),
    ("Mouse",50,150.00),
    ("keyboard",20,150.00),
    ("Monitor",10,3000.00)
]
print(inventory)
highest_value=0
for items in inventory:
    item_name,quantity,price=items
    total_price=quantity*price
    print("item is ",item_name,"the total price is ",total_price)
    if total_price>highest_value:
        highest_value=total_price
        item_with_highest_value=item_name
print("highest stock value is ",highest_value)
print("The item with highest stock value is ",item_with_highest_value)
