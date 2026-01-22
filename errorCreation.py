from Matrixclass import Matrix
import random

def random_error(codemessages):
    """simulates errors in code that happen because of noise"""
    #1 in 10 occurence of 2 mistakes
    twochanges = random.randint(0,9)   
    codemessage = random.choice(codemessages)
    #when 2 mistakes occur somewhere in the list of codes 
    if twochanges == 0 and codemessage.kolommen >= 2:
        #randomly chose error location
        #codemessage = codemessages[random.randint(0, len(codemessages)-1)]
        places = random.sample(range(0,codemessage.kolommen), 2) 

        #Fix the error on 2 places
        codemessage.vorm[places[0]][0] = 1 - codemessage.vorm[places[0]][0]   
        codemessage.vorm[places[1]][0] = 1 - codemessage.vorm[places[1]][0]
        return codemessages 

    #when only 1 mistake occurs in each code:
    else:
        for codemessage in codemessages: 
            place = random.randint(0, codemessage.kolommen-1)    
            codemessage.vorm[place][0] = 1 - codemessage.vorm[place][0]

        #output is list of matrices 
        return codemessages
