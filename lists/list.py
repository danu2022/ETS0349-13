myList = ["python", "c++", "javascript"]
print(myList) # output ["python", "c++", "javascript"]
print(myList[1]) # output "c++"
print(myList[:2]) # output ['python', 'c++']

myList[1] = "c#"
print(myList) # output ['python', 'c#', 'javascript']

# To add an item to the end of the list
myList.append("go")

print(myList) # output ['python', 'c#', 'javascript', 'go']

#If there are more than one item with the specified value, the remove() method removes the first occurrence:
myList.remove("c#")

print(myList) # output ['python', 'javascript', 'go']