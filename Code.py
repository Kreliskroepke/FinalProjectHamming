def main():
    message = "hi"
    codemessages = encode(message) 
    #verstuur/test de code door walkie_talkie(codemessages) 
    receivedmessage = decode(codemessages)
    return receivedmessage

class Matrix:
    def __init__(self, vorm):
        self.vorm = vorm
        self.rijen = len(vorm)
        self.kolommen = len(vorm[0])
    
    def __str__(self):
        return str(self.vorm)

    #To print a matrix inside a list
    def __repr__(self):
        return str(self.vorm)

    #define addition
    def __add__(self,other):
        if isinstance(other, Matrix):
            if self.rijen != other.rijen or self.kolommen != other.kolommen:
                #thanks stackexchange
                raise ValueError("The matrices aren't the same size")
            else: 
                #empty matrix with the same dimensions
                result = Matrix(self.nulmatrix_maker(self.rijen, self.kolommen))

                #for all rows
                for i in range(self.rijen):
                    #for all columns
                    for j in range(self.kolommen):
                        result.vorm[i][j] = (self.vorm[i][j] + other.vorm[i][j]) % 2
            return result
        else:
            raise ValueError("The matrix can't be added due to a wrong type")

    #define multiplication
    def __mul__(self, other):
        if isinstance(other, Matrix):
            #Columns of A must match the rows of B
            if self.kolommen != other.rijen:
                raise ValueError("The matrices have the wrong sizes")
            else:
                resultaat = Matrix(self.nulmatrix_maker(self.rijen, other.kolommen))

            for i in range(self.rijen):
                for j in range(other.kolommen):
                    som = 0
                    for k in range(self.kolommen):
                        som += self.vorm[i][k] * other.vorm[k][j]
                    resultaat.vorm[i][j] = som % 2
            return resultaat

        #For convenience, (M * list), encode already turns the lists into matrices, so this is for tests
        elif isinstance(other,list):
            if len(other) != self.kolommen:
                raise ValueError("The matrix and list have the wrong sizes")
            temp_vector = Matrix([[int(x) % 2] for x in other])
            return self * temp_vector
        
        #scalar multiplication for ints and floats
        elif isinstance(other, int):
            resultaat = Matrix(self.nulmatrix_maker(self.rijen, self.kolommen))
            for i in range(self.rijen):
                for j in range(self.kolommen):
                    resultaat.vorm[i][j] = (self.vorm[i][j] * other) % 2
            return resultaat
        elif isinstance(other, float): 
            resultaat = Matrix(self.nulmatrix_maker(self.rijen, self.kolommen))
            for i in range(self.rijen):
                for j in range(self.kolommen):
                    resultaat.vorm[i][j] = (self.vorm[i][j] * other) % 2
            return resultaat
        #if the other isnt a scalar or matrix, then error
        else:
            raise ValueError("The matrix can't be multiplied due to a wrong type")

    #(scalar * M)    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def transpose(self):
        resultaat = Matrix(self.nulmatrix_maker(self.kolommen, self.rijen))

        for i in range(self.kolommen):
            for j in range(self.rijen):
                resultaat.vorm[i][j] = self.vorm[j][i]
        return resultaat

    #method om van G-matrix de parity matrix H te maken
    def parity(self): 
        parity_matrix = []
        bit_base = self.kolommen - self.rijen #afhankelijk van r, niet van n
        getallen = self.kolommen 
        for i in range(1,getallen+1):
            binaire_getal = format(i, f"0{bit_base}b")
            kolom = [int(bit) for bit in binaire_getal]
            parity_matrix.append(kolom)
        return Matrix(parity_matrix).transpose()

    #we define a method to make zero-matrices, to do all matrix-transformations
    @staticmethod
    def nulmatrix_maker(k,n):
        n=int(n) #n is kolom
        k=int(k) #k is rij
    
        nulmatrix = []
        for i in range(0,k):
            extrarow = [0] * n
            nulmatrix.append(extrarow)
        
        return nulmatrix
        
#Standard Gen matrix from Wikipedia, voor nu global variable, wordt class variable oid
G = Matrix([
    [1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 1]
])
G_T = G.transpose()

#dit zit boven de encode want hij kent binaryconvert(tekst) anders niet
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

def encode(tekst):
    codemessages = []
    knabbellijst = binaryconvert(tekst)
    for i in knabbellijst:
        if G_T.kolommen != len(i):
            raise ValueError("The length of the knabbel doesn't coincide with the dimensions of G")
        else:
            p_vector = Matrix([[int(char)] for char in i])
            codemessage = G_T * p_vector
            codemessages.append(codemessage)
    return codemessages

#werkt nog niet helemaal, working on it 
def decode(codemessages):
    H = G.parity()                 # ik moet dit nog even goed checken
    R = Matrix([                   # R wordt nog G.decoder 
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1]
    ])
    allnibbles = []

    for codemessage in codemessages:
        vector = H * codemessage
        if not is_zero_matrix(vector):
            codemessage = correct(codemessage)   # def correct moet nog geschreven
        receivednibble = R * codemessage
        allnibbles.append(receivednibble)

    receivedmessage = convert_to_string(allnibbles)  # def convert_to_string nog schrijven
    return receivedmessage
 #done   
def correct(codemessage, G):
    H = Matrix(G).parity()
    codemessage = Matrix(codemessage)
    error_position = position(H*codemessage)
    if codemessage[error_position-1]==0:
        codemessage[error_position-1]=1
    else:
        codemessage[error_position-1]=0
    
    if position(H*codemessage) != 0:
        raise ValueError("The message has 2 in one letter")
    else:
        return codemessage
    
#done
def position(vector):
    #vector als [0,0,0]
    num = vector[0][0]
    for i in vector:
        num = num*2 + i
    return (num)
    
#return the knabbels to strings of binary
def convert_to_string(allknabbels):
    decodedmessage = ""
    tempmessage = ""
    binarymessage = ""
    for i in range(len(allknabbels)):
        for j in allknabbels[i].vorm:
            binarymessage += str(row[0])
    
    for char in binarymessage:
        tempmessage += char
        if len(tempmessage) == 8:
            ascii_value = int(tempmessage, 2)
            chara = chr(ascii_value)
            decodedmessage += chara
            tempmessage = ""
            continue
    return decodedmessage

#replacement of np.all() 
def is_zero_matrix(mat):
    for row in mat.vorm:
        for value in row:
            if value != 0:
                return False
    return True
    
#dit is wat de Harvard filmpjes guy doet om de code goed importeerbaar te maken en later unit tests te kunnen draaien
if __name__ == "__main__":
    main()

