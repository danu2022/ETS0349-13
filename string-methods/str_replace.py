txt = "I am learning python"

x = txt.replace("python", "c++") # returns the new str that replaces the string python with c++
y = txt.replace("nostr", "c++") # returns the previous str because there is no 'nostr' in txt

print(x) # I am learning c++ output
print(y) # I am learning python output