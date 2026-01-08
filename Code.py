import numpy as np

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

#Standard Gen matrix from wikipedia
G = np.array([
    [1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 1]
])

G_T = G.transpose()
print(G_T)
