from Matrixclass import Matrix

def isZeroMatrix(mat):
    """Checks if a matrix is all zero's"""
    for row in mat.vorm:
        for value in row:
            if value != 0:
                return False
    return True

def position(vector): 
    """takes vector, returns binary number that it forms"""
    num = 0
    for i in range(vector.rijen-1, -1, -1): 
        num = (num*2 + vector.vorm[i][0])
    return (num)     #output is integer

def correct(codemessage, H): 
    """checks if message has errors and corrects them"""
    error_position = position(H*codemessage)

    #switch the bits from 0 to 1 and vice versa
    codemessage.vorm[error_position-1][0] = 1-codemessage.vorm[error_position-1][0]
    
    #for two mistakes:
    if position(H*codemessage) != 0:
        raise ValueError("The message has 2 errors in one letter")
    else:
        return codemessage     #output is matrix

def convertToString(all_knabbels): 
    """converts binary into text""" 
    k = len(allknabbels[0].vorm)
    b = k if k > 8 else 8 

    decodedmessage = []
    tempmessage = []

    for i in range(len(all_knabbels)):
        for row in all_knabbels[i].vorm:
            tempmessage.append(str(row[0]))

            #if your # of bits is 8 or k:
            if len(tempmessage) == b:
                ascii_value = int("".join(tempmessage), 2)
                decodedmessage.append(chr(ascii_value))
                #empty the templist
                tempmessage.clear()

    return "".join(decodedmessage) #output is str

def decode(codemessages, H, R):
    """takes list of codemessages, checks errors, corrects and translates to text, returns text message"""
    all_knabbels = []
    for codemessage in codemessages:
        vector = H * codemessage
        if not isZeroMatrix(vector):
            codemessage = correct(codemessage, H)   
        received_knabbel = R * codemessage
        all_knabbels.append(received_knabbel)

    receivedmessage = convertToString(all_knabbels)  
    return receivedmessage #output is text
