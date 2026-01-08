import numpy as np

class Matrix:
    def __init__(self, inputs):
        self.inputs = np.array(inputs)
        self.rijen = len(inputs)
        self.kolommen = len(inputs[0])
    
    def __str__(self):
        return str(self.inputs)
    
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
            return result
        else:
            raise ValueError("The matrix can't be added due to a wrong type")

    def __mul__(self, other):
        if isinstance(other, Matrix):
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
        else:
            raise ValueError("The matrix can't be multiplied due to a wrong type")

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


