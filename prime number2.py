number=int(input("enter the number:"))
prime="is prime"
for i in range(2,number//2+1):
    if number%i==0:
        prime="not prime"
print(f"{number} {prime}")