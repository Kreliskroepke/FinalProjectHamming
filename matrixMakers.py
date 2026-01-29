from Matrixclass import *

def G_matrix(r=3):
    """makes kxn generator matrix based on number of parity bits"""
    n = 2**r -1	#n is length of codemessage
    k = n - r 	#k is number of databits / length of knabbel

    #Ontop every 2**p in a codemessage, there comes a parity bit from 0 to r-1 (so r=3 has a parity on 2**0, 2**1 and 2**2)
    parity_positions = [2**p for p in range(r)]
    #on the places with no paritybit, there comes a databit
    data_positions = [d for d in range(1,n+1) if d not in parity_positions]
    
    G = Matrix.nulmatrixMaker(k,n)

    for row, databit in enumerate(data_positions):
        #Put 1 on each databit position
        G[row][databit-1] = 1 
        for p in range(r):
            parity_position = 2**p
            #put 1 on position where databit and parity_positions have a 1 on the same place with AND
            if databit & parity_position:
                G[row][parity_position-1] = 1
    G = Matrix(G)
    return G

def H_matrix(r=3):
    """makes rxn parity-check matrix based on number of parity bits"""
    n = 2**r -1

    H = Matrix.nulmatrix_maker(r,n)
    for column in range(1,n+1):
        bits = format(column, f"0{r}b")
        #swaps the bits such that it conforms to the matrix on wikipedia, this code can probably be better, but it works...
        bits = bits[::-1] 
        for row in range(r):
            H[row][column-1] = int(bits[row])
    H = Matrix(H)
    return H

def R_matrix(r=3):
    """makes kxn decoder matrix based on number of parity bits"""
    n = 2**r -1
    k = n - r
    
    parity_positions = [2**p for p in range(r)]
    data_positions = [d for d in range(1,n+1) if d not in parity_positions]
    
    R = Matrix.nulmatrix_maker(k,n)
    
    for row, databit in enumerate(data_positions):
        R[row][databit-1] = 1
    R = Matrix(R)
    return R
