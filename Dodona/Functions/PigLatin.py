import re

def pigword(str):
    klinker = ['a', 'e', 'u', 'i', 'o', 'A', 'E', 'U', 'I', 'O']
    hoofdletters = ['A', 'B', 'C' , 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower_str = str[0].lower() + str[1:]
    new_str = lower_str
    ll = False
    if str[0] in klinker:
        new_str += 'way'
        if str[0] in hoofdletters:
            new_str = new_str[0].upper() + new_str[1:]
            return new_str
        return new_str
    for x in lower_str:
        while x not in klinker:
            if len(lower_str) == 1:
                new_str = new_str + 'ay'
                break
            elif lower_str == 'll':
                if ll:
                    new_str += 'ay'
                ll = True
                break
            else:
                new_str += x
                new_str = new_str[1::]
                break
        else:
            if new_str[-1] == 'q' or new_str[-1] == 'Q':
                new_str += new_str[0]
                new_str = new_str[1::]
                new_str += 'ay'
                break
            else:
                new_str += 'ay'
                break

    if str[0] in hoofdletters and str[1] in hoofdletters and str[1] in klinker:
        new_str = new_str[0:-3] + new_str[-3:-2].upper() + new_str[-2:]
        return new_str
    elif str[0] in hoofdletters:
        new_str = new_str[0].upper() + new_str[1:]
        return new_str
    return new_str


def piglatin(str):
    tekens = ['!', ',', ':',"'", '.', '-', ' ', '?', '(', ')']
    new_str = str
    l = re.split('(\W+?)', new_str)
    for a in l:
        if a == '':
            l.remove(a)
    vertaalde_zin = ''
    for x in l:
        if x in tekens:
            vertaalde_zin += x
        else:
            vertaalde_zin += pigword(x)

    if vertaalde_zin[0] == ' ':
        return vertaalde_zin[1:]
    return vertaalde_zin