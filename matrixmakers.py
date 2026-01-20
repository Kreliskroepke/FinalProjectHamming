from Matrixclass import *

def G_matrix(r=3):
    """makes generator matrix based on number of parity bits"""
    n = 2**r -1	#n is lengte codewoord
    k = n - r 	#k is aantal databits

    parity_positions = [2**p for p in range(r)]
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
    """makes parity-check matrix based on number of parity bits"""
    n = 2**r -1

    H = Matrix.nulmatrix_maker(r,n)
    for column in range(1,n+1):
        bits = format(column, f"0{r}b")
        #draait de bit om zodat de matrix goed komt
        bits = bits[::-1] 
        for row in range(r):
            H[row][column-1] = int(bits[row])
    H = Matrix(H)
    return H

def R_matrix(r=3):
    """makes decoder matrix based on number of parity bits"""
    n = 2**r -1
    k = n - r
    
    parity_positions = [2**p for p in range(r)]
    data_positions = [d for d in range(1,n+1) if d not in parity_positions]
    
    R = Matrix.nulmatrix_maker(k,n)
    
    for row, databit in enumerate(data_positions):
        R[row][databit-1] = 1
    R = Matrix(R)
    return R
