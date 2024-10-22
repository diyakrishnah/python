'''
DATE:22/10/2024
AUTHOR:Diya krishna
VERSION:1.1
'''
temprature=float(input("Enter temprature:"))
Q=input("Is this in (C)elsius or (F)ahrenheit?")
if Q=='C':
    c="celsius"
else:
    f="fahrenheit"
ctemprature=0.0
if Q=='C':
    ctemprature=(9/5*temprature)+32
    (temprature,"Celsius is",ctemprature,"fahrenheit")
else:
    f="celsius"
    ctemp=5/9*(temprature-32)
print(temprature,"fahrenhieitis",ctemprature,"celcius")