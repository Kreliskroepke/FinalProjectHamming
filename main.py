def main():
    message = "hi"
    codemessages = encode(message) 
    #verstuur/test de code door walkie_talkie(codemessages) 
    receivedmessage = decode(codemessages)
    return receivedmessage
