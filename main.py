def main():
    message = "hi"
    codemessages = encode(message) 
    #verstuur/test de code door walkie_talkie(codemessages) 
    receivedmessage = decode(codemessages)
    return receivedmessage

    G = Matrix([
        [1, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 0, 1]
    ])
    G_T = G.transpose()
