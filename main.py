from decoderfunctions import * #contains: decode, correct, position, convert_to_string, is_zero_matrix
from encoderfunctions import * #contains: encode, binaryconvert
from errorCreation import random_error
from Matrixclass import Matrix
from matrixmakers import * #contains: G_matrix, H_matrix, R_matrix
from Window import Windowmaker

def main():
    """Main code, mainly for tests"""
    message = "hi"
    r = 3 #number of paritybits 
    G = G_matrix(r)
    G_t = G.transpose()
    H = H_matrix(r)
    R = R_matrix(r)

    codemessages = encode(message, G_t) 
    codemessages = random_error(codemessages) 
    receivedmessage = decode(codemessages, H, R)
    return receivedmessage

if __name__ == "__main__":
    Windowmaker()
