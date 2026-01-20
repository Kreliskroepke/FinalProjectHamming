def decode(codemessages):            #input is nu list of matrices
    H = G.parity()  
    R = Matrix([  
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1]
    ])
    allnibbles = []

    codemessages = Random(codemessages)
    for codemessage in codemessages:
        vector = H * codemessage.transpose()
        if not is_zero_matrix(vector):
            codemessage = correct(codemessage, H)   
        receivednibble = R * codemessage
        allnibbles.append(receivednibble)

    receivedmessage = convert_to_string(allnibbles)  
    return receivedmessage

def correct(codemessage, H):     #input = matrix, matrix
    codemessage = codemessage.transpose())     #codemessage is al matrix
    error_position = position(H*codemessage)
    codemessage.vorm[error_position-1] = 1 -codemessage.vorm[error_position-1] 
    
    if position(H*codemessage) != 0:
        raise ValueError("The message has 2 errors in one letter")
    else:
        return codemessage

  def position(vector):     #input = matrix
    #vector als [0,0,0]
    num = vector.vorm[0][0]    #je kunt matrix niet indiceren, dus heb er vector.vorm van gemaakt
    for i in vector:        #i is een list, geen bit, dus dit gaat niet goed nu
        num = num*2 + i
    return (num)

#return the knabbels to strings of binary
def convert_to_string(allknabbels):        #input = allknabbels is list met matrices
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

#replacement of np.all() 
def is_zero_matrix(mat):        #input= matrix
    for row in mat.vorm:
        for value in row:
            if value != 0:
                return False
    return True
