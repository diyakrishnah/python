'''
AUTHOR:Diya krishna
VERSION:1.1
DATE:08/10/2024
'''
from datetime import datetime
current_time=(datetime.now())
print(current_time)
format1=current_time.strftime("%Y-%m-%d %H:%M:%S")
print(format1)
format2=current_time.strftime("%m/%d/%Y")
print(format2)
format3=current_time.strftime("%A,%m %d,%Y")
print(format3)
format4=current_time.strftime("%A,%m %d,%Y %H:%M:%S %P")
print(format4)
format5=current_time.strftime("%A-%B-%d %I:%M:%S IST %Y")
print(format5)
print(current_time.isoformat())
Date=current_time.strftime("%d")
print("Date =",Date)
Time=current_time.strftime("%H:%M:%S")
print("Time =",Time)
month=current_time.strftime("%B")
print("Month =",month)
year=current_time.strftime("%Y")
print("Year =",year)