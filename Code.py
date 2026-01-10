"""
TO DO (even aanzet om overzicht te hebben over het proces), feel free to correct/aanpas

def matrix H en R
code schrijven om matrix H en R af te leiden uit matrix G (dit kan volgens de opdracht, nog uizoeken hoe)

def encode
deze neemt message (str) 
>> convert naar binary 
>> divide into nibbles 
>> neemt list van nibbles en doet voor elke nibble G*nibble = codemessage 
>> krijg lijst van codemessages (7 bits) als output?

def decode
deze neemt list code messages 
>> check elke code message (H*codemessage = getal) 
>> als getal != 0 naar error correction en als getal ==0 verder decoden 
>> gebruik matrix R om te decoden
>> convert terug naar string

def correct
hier kom je als er geen 0 uitkomt na vermenigvuldiging met H tijdens decoden
nog uitzoeken hoe te correcten

def randomlyconvert
write a code that randomly converts a given number of bits to test the code

als dit werkt moeten we het ook kunnen uitbreiden naar andere Hamming codes
dus dan verandert ook matrix G. je hebt bijv 15,11 en 31,26 dus principe zal hetzelfde zijn maar dan ingewikkelder?
"""

import numpy as np

class Matrix:
    def __init__(self, inputs):
        self.inputs = np.array(inputs)
        self.rijen = len(inputs)
        self.kolommen = len(inputs[0])
    
    def __str__(self):
        return str(self.inputs)

    #define addition
    def __add__(self,other):
        if isinstance(other, Matrix):
            if self.inputs.shape != other.inputs.shape:
                #thanks stackexchange
                raise ValueError("The matrices aren't the same size")
            else: 
                #empty matrix with the same dimensions
                result = np.zeros(self.inputs.shape, dtype=self.inputs.dtype)

                #for all rows
                for i in range(self.inputs.shape[0]):
                    #for all columns
                    for j in range(self.inputs.shape[1]):
                        result[i,j] = self.inputs[i,j] + other.inputs[i,j]
            return Matrix(result)
        else:
            raise ValueError("The matrix can't be added due to a wrong type")

    #define multiplication
    def __mul__(self, other):
        if isinstance(other, Matrix):
            #Columns of A must match the rows of B
            if self.inputs.shape[1] != other.inputs.shape[0]:
                raise ValueError("The matrices have the wrong sizes")
            else:
                resultaat = Matrix(np.zeros((self.rijen, other.kolommen),dtype=int))

            for i in range(self.rijen):
                for j in range(other.kolommen):
                    som = 0
                    for k in range(self.kolommen):
                        som += self.inputs[i][k] * other.inputs[k][j]
                    resultaat.inputs[i][j] = som % 2
            return resultaat

        #scalar multiplication for ints and floats
        elif isinstance(other, int):
            resultaat = Matrix(np.zeros((self.rijen, self.kolommen),dtype=int))
            for i in range(self.rijen):
                for j in range(self.kolommen):
                    resultaat.inputs[i][j] = (self.inputs[i][j] * other) % 2
            return resultaat
        elif isinstance(other, float):
            resultaat = Matrix(np.zeros((self.rijen, self.kolommen),dtype=int))
            for i in range(self.rijen):
                for j in range(self.kolommen):
                    resultaat.inputs[i][j] = (self.inputs[i][j] * other) % 2
            return resultaat
        #if the other isnt a scalar or matrix, then error
        else:
            raise ValueError("The matrix can't be multiplied due to a wrong type")

    def transpose(self):
        resultaat = Matrix(np.zeros((self.kolommen, self.rijen),dtype=int))

        for i in range(self.kolommen):
            for j in range(self.rijen):
                resultaat.inputs[i][j] = self.inputs[j][i]
        return resultaat

#takes the initial input, and turns it into a list of nibbles
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

#Standard Gen matrix from Wikipedia
G = np.array([
    [1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 1]
])
G_T = G.transpose()

"""
def MultofMWithNibble():
    #verander dit nog naar de bit waarover we het hebben, is voorbeeld; verander ook functie input
    bleh = '0100'
    #turn nibble into vector 4x1
    p_vector = np.array([int(char) for char in bleh])
    templist = []
    
    for i in G_T:
        asdf = 0
        for j in range(4):
            #1 * first bit + 1 * second bit + 0 * third bit + 1 * fourth bit = first element of new matrix
            asdf += (i[j] * p_vector[j])
        templist.append(asdf % 2)
    templist = [int(x) for x in templist]
    templist = np.array(templist)
    return templist
"""
