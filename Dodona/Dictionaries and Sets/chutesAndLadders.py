chutes = {98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 47: 26, 16: 6}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def merge(chutes,ladders):
    try:
        for x, y in chutes.items():
            if x <= y:
                raise AssertionError
            for a, b in ladders.items():
                if a >= b:
                    raise AssertionError 
                elif x == a:
                    raise AssertionError            
        dictornary_number_spaces = chutes | ladders
        for x, y  in dictornary_number_spaces.items():
            difference = y - x
            dictornary_number_spaces[x] = difference
        return dictornary_number_spaces
    except AssertionError as exc:
        raise AssertionError('invalid configuration') from exc

def spaces(rolls, config_chutes, config_ladders):
    space = 0
    spaces_list = []
    chutes_ladders = merge(config_chutes, config_ladders)
    for x in rolls:
        if space + x > 100:
            continue
        if space in chutes_ladders:
            space = chutes_ladders[x]
        else:
            space += x
        spaces_list.append(space)        
    return spaces_list





