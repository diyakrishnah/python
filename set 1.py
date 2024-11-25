'''AUTHOR:Diya 
Date:25/11/2024'''
inventory={"A","B","C","D"}
new_item={"D","E","F","G","H"}
inventory.update(new_item)
print("updated inventory:",inventory)

#Dictionary
student={
"name":"Diya",
"age":17,
"course":["Engineering","CSE"]
}
print(student["name"])
student["age"]=18
student["grade"]="A"
print(student["grade"])
print(student["age"])
student.pop("grade","Key not found")
print(student.keys())
print(student.values())
print(student.items())
student_copy=student.copy()
print(student_copy)