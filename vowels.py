'''diya krishna
version 1.1
date29/10/2024'''
string_input=input("Enter a string:")
vowels="AEIOUaeiou"
vowel_count=0
for charector in string_input:
    if charector in vowels:
        vowel_count+=1
print(f" Number of  vowels in the given string {string_input}is ={vowel_count}")