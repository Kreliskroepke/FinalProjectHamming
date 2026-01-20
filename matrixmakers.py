from Matrixclass import *

def G_matrix(r=3):
    """makes kxn generator matrix based on number of parity bits"""
    n = 2**r -1	#n is length of codemessage
    k = n - r 	#k is number of databits / length of knabbel

    #op elke 2**p in een codemessage komt een parity bit van 0 tot r-1 (dus bij r=3 komt er parity op 2**0, 2**1 en 2**2)
    parity_positions = [2**p for p in range(r)]
    #op plekken waar geen parity bit staat komt een databit
    data_positions = [d for d in range(1,n+1) if d not in parity_positions]
    
    G = Matrix.nulmatrix_maker(k,n)

    for row, databit in enumerate(data_positions):
        #zet 1 op elke databit positie
        G[row][databit-1] = 1 
        for p in range(r):
            parity_position = 2**p
            #zet 1 op positie waar databit en parity_positions op dezelfde plek een 1 hebben met &
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
        #draait de bit om zodat de matrix wikipedia-stijl komt, deze code kan vast handiger, maar dit werkt...
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
