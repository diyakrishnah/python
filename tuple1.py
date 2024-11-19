'''AUTHOR:Diya krishna
'''
fruits=("banana","cherry","mango","apple","orange")
nuts=("almond","pista","cashew")
print(fruits[3])
print(nuts[-1])
print(len(fruits))
#concactination
combained=fruits+nuts
print(combained)
#repeat
repeat=(nuts)*4
print(repeat)
#membership
even=(2,4,6,8,10)
composite=(4,6,8)
print(4 in (even and composite))
#sliced
colours=("red","yellow","blue","black","pink")
print(colours[:3])
print(colours[2:])
print(colours[2:5])
print(colours[-3:])
#unpack into variables
person=("Anna",22,"Doctor")
name,age,profession=person
print("name:",name)
print("age :",age)
print("working as ",profession)
#
items=[("pen",50,5),("pencil",10,3),("scale",6,5)]
for stationary in items:
    stationary_name,quantity,price=stationary
    total_price=quantity*price
    print(total_price)
    print(stationary_name,quantity,price)



