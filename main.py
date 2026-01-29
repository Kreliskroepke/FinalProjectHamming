from decoderFunctions import * #contains: decode, correct, position, convertToString, isZeroMatrix
from encoderFunctions import * #contains: encode, binaryConvert
from errorCreation import randomError
from Matrixclass import Matrix
from matrixMakers import * #contains: G_matrix, H_matrix, R_matrix
from window import windowmaker

def main():
    """Main code, mainly for tests"""
    message = "hi"
    r = 3 #number of paritybits 
    G = G_matrix(r)
    G_t = G.transpose()
    H = H_matrix(r)
    R = R_matrix(r)

    codemessages = encode(message, G_t) 
    codemessages = randomError(codemessages) 
    receivedmessage = decode(codemessages, H, R)
    return receivedmessage

if __name__ == "__main__":
    windowmaker()
