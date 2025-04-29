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
print(thisdict) 
# output {'name': 'daniel', 'sex': 'male', 'age': 50, 'student':True}

thisdict.update({"acadamicyear": "3rd"}) # adds acadamicyear key value pair from dic
print(thisdict) 
# output {'name': 'daniel', 'sex': 'male', 'age': 50, 'student':True, 'acdamicyear':'3rd'}


thisdict.update({"age": 40}) # udaptes ages value from 50 to 40
print(thisdict) 
# output {'name': 'daniel', 'sex': 'male', 'age': 40, 'student':True, 'acdamicyear':'3rd'}

thisdict.pop("acadamicyear") # removes acadamicyear key value pair from dic
print(thisdict)
# output {'name': 'daniel', 'sex': 'male', 'age': 40, 'student':True}

thisdict.popitem() # removes the last key value pair from dic and in this case student
print(thisdict)
# output {'name': 'daniel', 'sex': 'male', 'age': 40, }

del thisdict["name"] # removes the last key value pair from dic and in this case name
print(thisdict)
# output {'sex': 'male', 'age': 40, }