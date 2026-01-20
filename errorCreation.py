import random

def Random(codemessages):            #input = list of matrices, matrix kun je niet indexeren, dus deze code gaat nu niet werken
    twochanges = random.randint(0,1)    #IK HEB RANDOM.CHOICE VERVANGEN DOOR RANDOM.RANDINT ANDERS WERKT HET NIET
    
    if twochanges == 1:
        line = random.randint(0, len(codemessages)-1)        #moet len(codemessages)-1 zijn?
        places = random.sample(range(0,len(place)), 2)        #deze place in len(place) bestaat niet, dus error 
        codemessages.vorm[line][places[0]] = 1 - codemessages.move[line][places[0]]     #KUNT GEEN MATRIX INDEXEREN, DAN MOET JE DE MATRIX.VORM GEBRUIKEN
        codemessages.vorm[line][places[1]] = 1 - codemessages.move[line][places[1]]
        return codemessages             
    else:
        for codemessage in codemessages:
            changes = random.randint(0,1)          
            if changes == 1:
                place = random.randint(0, len(codemessage)-1)    #WAT IS K? IS DAT LEN(CODEMESSAGE)?
                codemessage[place] = 1 - codemessage[place]
            else: 
                continue
        return codemessages         #output is list of matrices
