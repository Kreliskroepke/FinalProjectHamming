from Matrixclass import Matrix

def binaryconvert(tekst, k=4):                #input = str
    """takes text as input and returns a list of binary messages"""
    nibblelist = []
    bit_base = k 
    b = 2*k #2 keer de lengte van de databits
    for i in tekst:
        bits = format(ord(i), f'0{b}b')
        nibbles = [bits[j:j+bit_base] for j in range(0, b, bit_base)]
        for nibble in nibbles:
            nibble = [int(c) for c in nibble]
            nibblelist.append(nibble)
    return nibblelist                    #output nibblelist = [[ints],..]

def encode(tekst, G_t):      #input = str
    """takes a message, translates it to binary, and returns a list with codemessages"""
    codemessages = []
    k = G_t.kolommen
    knabbellijst = binaryconvert(tekst, k)
    for i in knabbellijst:
        if G_t.kolommen != len(i):
            raise ValueError("The length of the knabbel doesn't coincide with the dimensions of G")
        else:
            p_vector = Matrix([[int(char)] for char in i])
            codemessage = G_t * p_vector
            codemessages.append(codemessage)
    return codemessages                #output codemessages = list of Matrices IS DIT HANDIG?

def readableEncoder(nibblelist):
    """This prints a string of binary in segments of 4, for window"""
    Readable = ""
    for i in nibblelist:
        for j in i:
            Readable += str(j)
    return ' '.join(Readable[i:i+4] for i in range(0,len(Readable),4))
