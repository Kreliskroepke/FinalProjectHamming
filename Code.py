def binaryconvert(tekst):
    x = "Hello"
    nibblelist = []
    temp = ""

    #turn it into binary, text -> ASCII -> binary
    for char in x:
        b = ''.join(format(ord(char), '08b') for char in x)

    #chop into segments of 4 and put in a list
    for char in b:
        temp += char
        if len(temp) == 4:
            nibblelist.append(temp)
            temp = ""
    print(nibblelist)
