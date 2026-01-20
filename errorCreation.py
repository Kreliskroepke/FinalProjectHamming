import random

def Random(codemessages):            #input = list of matrices, matrix kun je niet indexeren, dus deze code gaat nu niet werken
    twochanges = random.randint(0,9)   
    
    if twochanges == 0:
        codemessage = codemessages[random.randint(0, len(codemessages)-1)]     
        places = random.sample(range(0,codemessage.kolommen), 2)  
        codemessage.vorm[0][places[0]] = 1 - codemessage.vorm[0][places[0]]     
        codemessage.vorm[0][places[1]] = 1 - codemessage.vorm[0][places[1]]
        return codemessages             
    else:
        for codemessage in codemessages:
            changes = random.randint(0,1)          
            if changes == 1:
                place = random.randint(0, codemessage.kolommen-1)    
                codemessage.vorm[0][place] = 1 - codemessage.vorm[0][place]
            else: 
                continue
        return codemessages         #output is list of matrices
