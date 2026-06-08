# ----- DICTINARIES -----
# dict() or {}


# - 1
dog = {}

# - 2
dog['name'] = "Simba"
dog["color"] = "Brown"
dog["breed"] = "Rotweiler"
dog["legs"] = 4
dog["age"] = 10

print(dog)

# - 3
student = {
    "first_name": "Oscar",
    "last_name": "Okereke",
    "gender": "male",
    "age": 24,
    "marital_status": "single",
    "skills": ["HTML", "CSS", "JavaScript", "React", "React-Native", "Kotlin"],
    "country": "Nigeria",
    "city": "Lagos",
    "address": "sangotedo"
}

# - 4
print(len(student))

# - 5
skill_value = student["skills"]
skill_value = student.get("skills")
print(type(skill_value))

# - 6
student["skills"].append("Node")
print(student)

# - 7
keys = student.keys()
print(keys)

# - 8
values = student.values()
print(values)

# - 9
dct_to_lst = student.items()
print(dct_to_lst)

# - 10
del student["skills"]
print(student)

# - 11
del dog
print(dog)



# ----- DONE -----