def omgekeerd(key):
    newDic = {v: k for k, v in key.items()}
    return newDic

def code39(i, ii):
    code = ""
    i = i.upper()
    for x in i:
        code = code + ii[x] + 's'
    code = code[:-1]
    return code 

def decode39(i, ii):
    teller = 0
    x = 0
    y = 9
    zin = ''
    new_ii = omgekeerd(ii)
    while teller < (len(i)//10 + 1):
        zin += new_ii[i[x:y]]
        teller += 1
        x += 10
        y += 10
    return zin