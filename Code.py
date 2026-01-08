x = "Hello"
nibblelist = []
temp = ""

for char in x:
    b = ''.join(format(ord(char), '08b') for char in x)
for char in b:
    temp += char
    if len(temp) == 4:
        nibblelist.append(temp)
        temp = ""
print(nibblelist)
