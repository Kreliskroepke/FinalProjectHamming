def encode(tekst):                        #input = str
    codemessages = []
    knabbellijst = binaryconvert(tekst)
    for i in knabbellijst:
        if G_T.kolommen != len(i):
            raise ValueError("The length of the knabbel doesn't coincide with the dimensions of G")
        else:
            p_vector = Matrix([[int(char)] for char in i])
            codemessage = G_T * p_vector
            codemessages.append(codemessage)
    return codemessages                #output codemessages = list of Matrices IS DIT HANDIG?
 
#dit zit boven de encode want hij kent binaryconvert(tekst) anders niet
#takes the initial input, and turns it into a list of nibbles
def binaryconvert(tekst):                #input = str
    nibblelist = []
    bit_base = 4 #dit moet in fase 2 afhankelijk worden van k
    
    for i in tekst:
        bits8 = format(ord(i), '08b')
        nibbles = [bits8[j:j+bit_base] for j in range(0, 8, bit_base)]
        for nibble in nibbles:
            nibble = [int(c) for c in nibble]
            nibblelist.append(nibble)
    return nibblelist                    #output nibblelist = [[ints],..]
