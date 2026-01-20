from decoderfunctions import * #contains: decode, correct, position, convert_to_string, is_zero_matrix
from encoderfunctions import * #contains: encode, binaryconvert
from errorCreation import Random
from Matrixclass import Matrix
from Window import windowmaker

G = Matrix([
    [1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 1]
])
G_T = G.transpose()

def main():
    message = "hi"
    codemessages = encode(message) 
    codemessages = Random(codemessages) 
    receivedmessage = decode(codemessages)
    return receivedmessage

main()
