from Matrixclass import Matrix

def binaryconvert(text, k=4):
    """takes text as input and returns a list of binary messages"""
    knabbel_list = []
    bit_base = k 
    b = k if k > 8 else 8
    for i in text:
        bits = format(ord(i), f'0{b}b')
        knabbels = [bits[j:j+bit_base] for j in range(0, b, bit_base)]
        for knabbel in knabbels:
            knabbel = [int(c) for c in knabbel]
            knabbel_list.append(knabbel)
    return knabbel_list

def encode(text, G_t):
    """takes a message, translates it to binary, and returns a list with codemessages"""
    codemessages = []
    k = G_t.kolommen
    knabbel_list = binaryconvert(tekst, k)
    for i in knabbel_list:
        if G_t.kolommen != len(i):
            raise ValueError("The length of the knabbel doesn't coincide with the dimensions of G")
        else:
            p_vector = Matrix([[int(char)] for char in i])
            codemessage = G_t * p_vector
            codemessages.append(codemessage)
    return codemessages     #output codemessages is list of matrices 

def readableEncoder(knabbel_list):
    """This prints a string of binary in segments of 4, for window"""
    Readable = ""
    for i in knabbel_list:
        for j in i:
            Readable += str(j)
    return ' '.join(Readable[i:i+4] for i in range(0,len(Readable),4))
