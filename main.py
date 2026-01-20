from decoderfunctions import * #contains: decode, correct, position, convert_to_string, is_zero_matrix
from encoderfunctions import * #contains: encode, binaryconvert
from errorCreation import random_error
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

    """
    LET OP ------ remove this comment when code is finished -----
    for code developing purposes, these are the matrices that the codes above produce (conform wikipedia):
    G = [[1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1]]
    G_t = [[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    H = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]]
    R = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]]

    LET OP MATRIX G IS GEEN GLOBAL VARIABLE MEER DUS JE MOET HEM MEEGEVEN MET DE CODE, HEB IK HIER IN MAIN EN (VOLGENS MIJ) OP ALLE RELEVANTE PLEKKEN NU OOK GEDAAN
    """

    codemessages = encode(message, G_t) 
    codemessages = random_error(codemessages) 
    receivedmessage = decode(codemessages, H, R)
    return receivedmessage

main()

"""
#dit is wat de Harvard filmpjes guy doet om de code goed importeerbaar te maken en later unit tests te kunnen draaien:

if __name__ == "__main__":
    main()
"""
