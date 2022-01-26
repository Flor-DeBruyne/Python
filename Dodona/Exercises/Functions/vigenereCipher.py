def codeer(str, code):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    x = len(str) // len(code) 
    y = len(str) % len(code)
    nul = 0
    sleutel_woord = ""
    teller = 0
    teller_overig = 0
    teller_index = 0
    antwoord = ''
    while teller is not x:
        sleutel_woord += code
        teller += 1
    new_sleutel_woord = sleutel_woord
    while teller_overig is not y:
        new_sleutel_woord += code[nul]
        nul += 1
        teller_overig += 1
    for x in str:
        if x in alpha:
            z = alpha.index(x) + alpha.index(new_sleutel_woord[teller_index])
            z %= 26
            antwoord += alpha[z]
        else:
            antwoord += x
        teller_index += 1
    return antwoord

def decodeer(str, code):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    x = len(str) // len(code) 
    y = len(str) % len(code)
    nul = 0
    sleutel_woord = ""
    teller = 0
    teller_overig = 0
    teller_index = 0
    antwoord = ''
    while teller is not x:
        sleutel_woord += code
        teller += 1
    new_sleutel_woord = sleutel_woord
    while teller_overig is not y:
        new_sleutel_woord += code[nul]
        nul += 1
        teller_overig += 1
    for x in str:
        if x in alpha:
            z = alpha.index(x) - alpha.index(new_sleutel_woord[teller_index])
            z %= 26
            antwoord += alpha[z]
        else:
            antwoord += x
        teller_index += 1
    return antwoord