woordenboek = {}

def vertalingToevoegen(woord, vertaling, dic):
    dic[woord] = vertaling

def vertaling(vertaling, dic):
    if vertaling in dic:
        return dic[vertaling]
    return '???'