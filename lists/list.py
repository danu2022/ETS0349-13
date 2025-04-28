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

#Insert the value "html" as the third element of the list:
myList.insert(2, "html")
print(myList) # output ['python', 'javascript', 'html', 'go']

#Remove the last element of the list
myList.pop()
print(myList) # output ['python', 'javascript', 'html']

#Reverse the order of the list:
myList.reverse()
print(myList) # output ['html', 'javascript', 'python']


numList = [5, 9, 1, 3, 10]
numList.sort()
print(numList) # output [1, 3, 5, 9, 10]