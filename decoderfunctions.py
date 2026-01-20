from Matrixclass import Matrix

def is_zero_matrix(mat):        #input= matrix
    """replaces np.all"""
    for row in mat.vorm:
        for value in row:
            if value != 0:
                return False
    return True

def position(vector):     #input = matrix
    """takes vector, returns binary number that it forms"""
    num = 0
    for i in range(vector.rijen-1, -1, -1): 
        num = (num*2 + vector.vorm[i][0])
 
    return (num) #output = number

def correct(codemessage, H):     #input = matrix, matrix
    """checks if message has errors and corrects them"""

    #position error
    error_position = position(H*codemessage)

    #switching bits
    codemessage.vorm[error_position-1][0] = 1-codemessage.vorm[error_position-1][0]
    
    #voor 2 fouten
    if position(H*codemessage) != 0:
        raise ValueError("The message has 2 errors in one letter")
    else:
        return codemessage #output = matrix

#return the knabbels to strings of binary
def convert_to_string(allknabbels):        #input = allknabbels is list met matrices
    """converts binary into text"""" 
    decodedmessage = ""
    tempmessage = ""
    binarymessage = ""
    for i in range(len(allknabbels)):
        for j in allknabbels[i].vorm:
            binarymessage += str(row[0])        #WAT IS ROW, moet j row zijn?
    
    for char in binarymessage:
        tempmessage += char
        if len(tempmessage) == 8:
            ascii_value = int(tempmessage, 2)
            chara = chr(ascii_value)
            decodedmessage += chara
            tempmessage = ""
            continue
    return decodedmessage        #output = nu lege string volgens mij?

def decode(codemessages, H, R):            #input is nu list of matrices
    """takes list of codemessages, checks errors, corrects and translates to text, returns text message"""
    allnibbles = []

    codemessages = codemessages
    for codemessage in codemessages:
        vector = H * codemessage.transpose()
        if not is_zero_matrix(vector):
            codemessage = correct(codemessage, H)   
        receivednibble = R * codemessage
        allnibbles.append(receivednibble)

    receivedmessage = convert_to_string(allnibbles)  
    return receivedmessage
