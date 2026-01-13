import numpy as np

class Matrix:
    def __init__(self, vorm):
        self.vorm = np.array(vorm)
        self.rijen = len(vorm)
        self.kolommen = len(vorm[0])
    
    def __str__(self):
        return str(self.vorm)

    #define addition
    def __add__(self,other):
        if isinstance(other, Matrix):
            if self.vorm.shape != other.vorm.shape:
                #thanks stackexchange
                raise ValueError("The matrices aren't the same size")
            else: 
                #empty matrix with the same dimensions
                result = np.zeros(self.vorm.shape, dtype=self.vorm.dtype)

                #for all rows
                for i in range(self.vorm.shape[0]):
                    #for all columns
                    for j in range(self.vorm.shape[1]):
                        result[i,j] = (self.vorm[i,j] + other.vorm[i,j]) % 2
            return Matrix(result)
        else:
            raise ValueError("The matrix can't be added due to a wrong type")

    #define multiplication
    def __mul__(self, other):
        if isinstance(other, Matrix):
            #Columns of A must match the rows of B
            if self.vorm.shape[1] != other.vorm.shape[0]:
                raise ValueError("The matrices have the wrong sizes")
            else:
                resultaat = Matrix(np.zeros((self.rijen, other.kolommen),dtype=int))

            for i in range(self.rijen):
                for j in range(other.kolommen):
                    som = 0
                    for k in range(self.kolommen):
                        som += self.vorm[i][k] * other.vorm[k][j]
                    resultaat.vorm[i][j] = som % 2
            return resultaat

        #scalar multiplication for ints and floats
        elif isinstance(other, int):
            resultaat = Matrix(np.zeros((self.rijen, self.kolommen),dtype=int))
            for i in range(self.rijen):
                for j in range(self.kolommen):
                    resultaat.vorm[i][j] = (self.vorm[i][j] * other) % 2
            return resultaat
        elif isinstance(other, float): 
            resultaat = Matrix(np.zeros((self.rijen, self.kolommen),dtype=int))
            for i in range(self.rijen):
                for j in range(self.kolommen):
                    resultaat.vorm[i][j] = (self.vorm[i][j] * other) % 2
            return resultaat
        #if the other isnt a scalar or matrix, then error
        else:
            raise ValueError("The matrix can't be multiplied due to a wrong type")

    def transpose(self):
        resultaat = Matrix(np.zeros((self.kolommen, self.rijen),dtype=int))

        for i in range(self.kolommen):
            for j in range(self.rijen):
                resultaat.vorm[i][j] = self.vorm[j][i]
        return resultaat

    #method om van G-matrix de parity matrix te maken
    def parity(self): 
        parity_matrix = []
        bit_base = self.rijen
        getallen = self.kolommen 
        for i in range(1,getallen+1):
            binaire_getal = format(i, f"0{bit_base}b")
            kolom = [int(bit) for bit in binaire_getal]
            parity_matrix.append(kolom)
        return Matrix(parity_matrix).transpose


#takes the initial input, and turns it into a list of nibbles
def binaryconvert(tekst):
    nibblelist = []
    bit_base = 4 #dit moet in fase 2 afhankelijk worden van k
    
    for i in tekst:
        bits8 = format(ord(i), '08b')
        nibbles = [bits8[j:j+bit_base] for j in range(0, 8, bit_base)]
        for nibble in nibbles:
            nibble = [int(c) for c in nibble]
            nibblelist.append(nibble)
    return nibblelist

#Standard Gen matrix from Wikipedia
G = Matrix([
    [1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 1]
])
G_T = G.transpose()
H = G.parity()


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
