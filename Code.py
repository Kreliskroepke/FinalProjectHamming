x = "Hello"

for char in x:
    b = ''.join(format(ord(char), '08b') for char in x)
print(b)
