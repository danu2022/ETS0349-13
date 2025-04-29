thisdict = {
  "name": "daniel",
  "sex": "male",
  "age": 50
}

print(thisdict) # output {'name': 'daniel', 'sex': 'male', 'age': 50}
print(thisdict["age"]) #output 50

keys = thisdict.keys()
print(keys) # output dict_keys(['name', 'sex', 'age'])

values = thisdict.values()
print(values) # output dict_values(['daniel', 'male', 50])

# Adding items in to dictionary

thisdict["student"] = True
print(thisdict) # output {'name': 'daniel', 'sex': 'male', 'age': 50, 'student':True}

thisdict.update({"acdamicyear": "3rd"})
print(thisdict) # output {'name': 'daniel', 'sex': 'male', 'age': 50, 'student':True, 'acdamicyear':'3rd'}