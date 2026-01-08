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

def MultofMWithNibble():
    #verander dit nog naar de bit waarover we het hebben, is voorbeeld; verander ook functie input
    bleh = '0100'
    #turn nibble into vector 4x1
    bleh_vec = np.array([int(char) for char in bleh])
    templist = []
    
    for i in G_T:
        asdf = 0
        for j in range(4):
            #1 * first bit + 1 * second bit + 0 * third bit + 1 * fourth bit = first element of new matrix
            asdf += (i[j] * bleh_vec[j])
        templist.append(asdf)
    templist = [int(x) for x in templist]
