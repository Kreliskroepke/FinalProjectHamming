from decoderFunctions import * #contains: decode, correct, position, convertToString, isZeroMatrix
from encoderFunctions import * #contains: encode, binaryConvert
from errorCreation import randomError
from Matrixclass import Matrix
from matrixMakers import * #contains: G_matrix, H_matrix, R_matrix
from window import windowmaker

def main():
    """Runs the GUI version of the program"""
    r = 3                               #number of paritybits, adjust this number to run different Hamming(n,k) codes
    windowmaker(r)

def runHamming():
    """Runs without opening GUI"""
    message = "bit+wise-operator101"    #make sure this message corresponds with the message in bitwise.py
    r = 3                               #make sure r (the number of parity bits) corresponds with the value of r in bitwise.py 
    G = G_matrix(r)
    G_t = G.transpose()
    H = H_matrix(r)
    R = R_matrix(r)

    codemessages = encode(message, G_t) 
    codemessages = randomError(codemessages) 
    receivedmessage = decode(codemessages, H, R)
    
    return receivedmessage

if __name__ == "__main__":
    main()
