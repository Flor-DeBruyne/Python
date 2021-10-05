boek = 24.95 
aantal=60
korting = boek * .4
zonder = ((boek - korting) * aantal)


def bereken(): #functions start with def
    for x in range(aantal): #for loop for specified amount 'range(start,stop,itteration)'
        if x==0:
          met = zonder +3 
        else:
          met +=.75    
    return met

bereken()