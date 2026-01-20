from decoderfunctions import * #contains: decode, correct, position, convert_to_string, is_zero_matrix
from encoderfunctions import * #contains: encode, binaryconvert
from errorCreation import Random
from Matrixclass import Matrix
from matrixmakers import * #contains: G_matrix, H_matrix, R_matrix
from Window import windowmaker

def main():
    message = "hi"
    r = 3 #aantal parity bits

    G = G_matrix(r)
    G_t = G.transpose()
    H = H_matrix(r)
    R = R_matrix(r)
    
    codemessages = encode(message, G_t) 
    codemessages = Random(codemessages) 
    receivedmessage = decode(codemessages, H, R)
    return receivedmessage

main()

"""
#dit is wat de Harvard filmpjes guy doet om de code goed importeerbaar te maken en later unit tests te kunnen draaien
if __name__ == "__main__":
    main()
"""
