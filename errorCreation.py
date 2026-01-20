import random
#verbeterde versie
def random_error(codemessages): #hoofdletter maakt het class, random overschrijft de andere random, dus heb m random_error genoemd en aangepast in main
    """simulates errors in code that happen because of noise"""
    # 1 in 10 accurence of 2 mistakes
    twochanges = random.randint(0,9)   

    #when 2 mistakes accure somewhere in the list of codes 
    if twochanges == 0:
        #locatie willekeurig kiezen 
        codemessage = codemessages[random.randint(0, len(codemessages)-1)]
        places = random.sample(range(0,codemessage.kolommen), 2) 

        #aanpassen op 2 plaatsen
        codemessage.vorm[places[0]][0] = 1 - codemessage.vorm[places[0]][0]   
        codemessage.vorm[places[1]][0] = 1 - codemessage.vorm[places[1]][0]
        return codemessages 

    #when only 1 and 0 mistakes accure in each code
    else:
        # determine if 1 or 0 mistakes happen per code
        for codemessage in codemessages: 
            changes = random.randint(0,1)  

            #change bit for 1 mistake 
            if changes == 1:
                place = random.randint(0, codemessage.kolommen-1)    
                codemessage.vorm[place][0] = 1 - codemessage.vorm[place][0]
                
            # for no mistake in code 
            else: 
                continue

        # output list of matrices 
        return codemessages
