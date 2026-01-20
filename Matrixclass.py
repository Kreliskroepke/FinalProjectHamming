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
        
        return nulmatrix        #output is een list
